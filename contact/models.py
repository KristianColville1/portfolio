import uuid
from django.db import models
from django.core.mail import send_mail
from django.conf import settings


class UserQuery(models.Model):
    """
    UserQuery Model for users interaction and feedback
    """
    name = models.CharField(max_length=80)
    email = models.CharField(max_length=320, unique=False)
    comment = models.TextField()
    user_query_number = models.CharField(max_length=254,
                                         null=False,
                                         blank=False,
                                         default='')
    is_open = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'User Queries'

    def _generate_user_query_number(self):
        """
        Private Method generates a random, unique user query number using UUID
        """
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        """
        Overrides the original save method to set the user query number
        if it hasn't been set already.
        """
        if not self.user_query_number:
            self.user_query_number = self._generate_user_query_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.user_query_number


class QueryResponse(models.Model):
    """
    Query Response class allows super users to reply to user query.
    """
    ticket = models.OneToOneField(UserQuery,
                                  on_delete=models.CASCADE,
                                  related_name='user_query_response')
    reply = models.TextField()
    resolved = models.BooleanField(default=False)

    def _send_reply_to_email(self):
        """
        Private method sends users a reply to their email
        """
        their_email = self.ticket.email
        subject = 'Noreply - Query: ' + self.ticket.user_query_number
        body = self.reply

        send_mail(subject, body, settings.DEFAULT_FROM_EMAIL, [their_email])

    def save(self, *args, **kwargs):
        """
        Overrides the original save method to send a reply to the user
        if it hasn't been set already and sent. Only sends the reply if
        the superuser has resolved the issue.
        """
        if self.resolved is True:
            self._send_reply_to_email()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.reply

