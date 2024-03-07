from django.contrib import admin
from django.contrib.auth import get_user_model

from petstagram.accounts.forms import PetstagramUserCreateForm, PetstagramChangeForm

UserModel = get_user_model()


# Register your models here.


@admin.register(UserModel)
class AppUserAdmin(admin.ModelAdmin):
    model = UserModel
    add_form = PetstagramUserCreateForm
    form = PetstagramChangeForm
    list_display = ('pk', 'email', 'is_staff', 'is_superuser')
    search_fields = ('email',)
    ordering = ('pk',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ()}),
        ('Permissions', {'fields': ('is_active', 'is_staff',
                                    'groups', 'user_permissions')
        }),
        ('Important dates', {'fields': ('last_login',)
        }),)
    add_fieldsets = ((None,
                      {"classes": ("wide",),
                       "fields":
                           ("email",
                            "password1",
                            "password2"),
                       },),)
