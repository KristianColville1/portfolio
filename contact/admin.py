from django.contrib import admin
from .models import (UserQuery, QueryResponse)


class QueryResponseAdmin(admin.TabularInline):
    """
    UserQueryAdmin provides me with the ability to see and respond to queries.
    """
    model = QueryResponse
    list_display = [field.name for field in QueryResponse._meta.get_fields()]
    search_fields = [field.name for field in QueryResponse._meta.get_fields()]


@admin.register(UserQuery)
class UserQueryAdmin(admin.ModelAdmin):
    """
    UserQueryAdmin.
    """
    model = UserQuery
    list_display = [field.name for field in UserQuery._meta.get_fields()]
    search_fields = [field.name for field in UserQuery._meta.get_fields()]
    inlines = [QueryResponseAdmin]