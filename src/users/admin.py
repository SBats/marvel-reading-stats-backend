"""
Override standard user admin contribution
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from users.models import MarvelUser, Avatar


class MarvelUserInline(admin.StackedInline):
    """
    Define an inline admin descriptor for MarvelUser model
    which acts a bit like a singleton
    """
    model = MarvelUser
    can_delete = False
    verbose_name_singular = 'marvel user'
    verbose_name_plural = 'marvel users'


class UserAdmin(BaseUserAdmin):
    """
    Define a new User admin
    """
    inlines = (MarvelUserInline,)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Avatar)
