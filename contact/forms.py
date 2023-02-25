from django import forms
from .models import UserQuery


class ContactUsForm(forms.ModelForm):
    """
    Contact Us Form for submitting user queries to finechop
    """

    class Meta:
        model = UserQuery
        fields = (
            'name',
            'email',
            'comment',
        )
        exclude = ('user_query_number', 'is_open')

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Name',
            'email': 'Email',
            'comment':
            'Enter your query/feedback here and I will be in touch..',
        }
        self.fields['name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} '
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False
