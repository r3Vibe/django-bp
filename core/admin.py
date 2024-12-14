# Basic Imports
from django.contrib import admin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model

# Core App Imports
from core.forms import CustomUserCreationForm, SocialAppFormCustom

# Third Party Imports

## Import Export Package
from import_export.admin import ImportExportModelAdmin

## Unfold Package
from unfold.contrib.import_export.forms import ExportForm, ImportForm
from unfold.contrib.filters.admin import RangeDateFilter
from unfold.admin import ModelAdmin

## Simple History Package
from simple_history.admin import SimpleHistoryAdmin

## Guardin Package
from guardian.admin import GuardedModelAdmin

## Easy Audit Package
from easyaudit.admin import CRUDEventAdmin, LoginEventAdmin, RequestEventAdmin
from easyaudit.models import CRUDEvent, LoginEvent, RequestEvent

## Allauth Package
from allauth.account.models import EmailAddress
from allauth.account.admin import EmailAddressAdmin as BaseEmailAddressAdmin
from allauth.socialaccount.models import SocialAccount, SocialToken, SocialApp
from allauth.socialaccount.admin import SocialAccountAdmin as BaseSocialAccountAdmin
from allauth.socialaccount.admin import SocialTokenAdmin as BaseSocialTokenAdmin
from allauth.socialaccount.admin import SocialAppAdmin as BaseSocialAppAdmin
from allauth.usersessions.models import UserSession
from allauth.usersessions.admin import UserSessionAdmin as BaseUserSessionAdmin


# Unregister the Default Models
admin.site.unregister(Group)
admin.site.unregister(CRUDEvent)
admin.site.unregister(LoginEvent)
admin.site.unregister(RequestEvent)
admin.site.unregister(EmailAddress)
admin.site.unregister(SocialAccount)
admin.site.unregister(SocialToken)
admin.site.unregister(SocialApp)
admin.site.unregister(UserSession)


# Register with Unfold ModelAdmin
@admin.register(get_user_model())
class UserAdmin(
    BaseUserAdmin,
    ModelAdmin,
    ImportExportModelAdmin,
    SimpleHistoryAdmin,
    GuardedModelAdmin,
):
    list_filter_submit = True
    import_form_class = ImportForm
    export_form_class = ExportForm
    add_form = CustomUserCreationForm
    list_display = (
        "email",
        "first_name",
        "last_name",
        "is_staff",
        "is_superuser",
        "is_active",
    )
    list_editable = (
        "is_active",
        "is_staff",
        "is_superuser",
    )
    search_fields = (
        "email",
        "first_name",
        "last_name",
    )
    list_filter = (
        "is_staff",
        "is_superuser",
        "is_active",
        ("last_login", RangeDateFilter),
        ("created_at", RangeDateFilter),
    )
    filter_horizontal = (
        "groups",
        "user_permissions",
    )
    list_display_links = (
        "email",
        "first_name",
        "last_name",
    )
    ordering = ("created_at",)
    readonly_fields = (
        "created_at",
        "updated_at",
        "last_login",
    )

    fieldsets = (
        (
            "Personal info",
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "email",
                )
            },
        ),
        (
            "Status",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                )
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (
            "Important dates",
            {
                "fields": (
                    "last_login",
                    "created_at",
                    "updated_at",
                )
            },
        ),
    )
    add_fieldsets = (
        (
            "Personal info",
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "email",
                )
            },
        ),
        (
            "Password",
            {
                "fields": (
                    "password1",
                    "password2",
                )
            },
        ),
        (
            "Status",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                )
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (
            "Important dates",
            {
                "fields": (
                    "last_login",
                    "created_at",
                    "updated_at",
                )
            },
        ),
    )


@admin.register(Group)
class GroupAdmin(BaseGroupAdmin, ModelAdmin):
    warn_unsaved_form = True


@admin.register(CRUDEvent)
class CRUDEVentAdmin(CRUDEventAdmin, ModelAdmin):
    pass


@admin.register(RequestEvent)
class RequestEVentAdmin(RequestEventAdmin, ModelAdmin):
    pass


@admin.register(LoginEvent)
class LoginEVentAdmin(LoginEventAdmin, ModelAdmin):
    pass


@admin.register(SocialAccount)
class SocialAccountAdmin(BaseSocialAccountAdmin, ModelAdmin):
    def has_add_permission(self, request):
        """can not add and removes the add buttion from ui"""
        return False


@admin.register(EmailAddress)
class EmailAddressAdmin(BaseEmailAddressAdmin, ModelAdmin):
    pass


@admin.register(SocialToken)
class SocialTokenAdmin(BaseSocialTokenAdmin, ModelAdmin):
    pass


@admin.register(SocialApp)
class SocialAppAdmin(BaseSocialAppAdmin, ModelAdmin):
    form = SocialAppFormCustom


@admin.register(UserSession)
class UserSessionAdmin(BaseUserSessionAdmin, ModelAdmin):
    def has_add_permission(self, request):
        """can not add and removes the add buttion from ui"""
        return False
