from django.templatetags.static import static
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

UNFOLD = {
    "SITE_TITLE": "Django BP",
    "SITE_HEADER": "Django BP",
    "SHOW_LANGUAGES": True,
    "DASHBOARD_CALLBACK": "core.views.dashboard_callback",
    "SITE_URL": "/",
    "SITE_ICON": {
        "light": lambda request: static("icon-light.svg"),  # light mode
        "dark": lambda request: static("icon-dark.svg"),  # dark mode
    },
    "SITE_LOGO": {
        "light": lambda request: static("logo-light.svg"),  # light mode
        "dark": lambda request: static("logo-dark.svg"),  # dark mode
    },
    "SITE_SYMBOL": "speed",  # symbol from icon set
    "SITE_FAVICONS": [
        {
            "rel": "icon",
            "sizes": "32x32",
            "type": "image/svg+xml",
            "href": lambda request: static("favicon.svg"),
        },
    ],
    # Supported icon set: https://fonts.google.com/icons
    "SIDEBAR": {
        "show_search": True,
        "show_all_applications": False,
        "navigation": [
            {
                "separator": True,
                "collapsible": False,
                "items": [
                    {
                        "title": _("Dashboard"),
                        "icon": "dashboard",
                        "link": reverse_lazy("admin:index"),
                    },
                ],
            },
            {
                "title": _("User & Groups"),
                "separator": True,
                "collapsible": True,
                "items": [
                    {
                        "title": _("Users"),
                        "icon": "group",
                        "link": reverse_lazy("admin:core_user_changelist"),
                    },
                    {
                        "title": _("Sessions"),
                        "icon": "groups",
                        "link": "/admin/usersessions/usersession/",
                    },
                    {
                        "title": _("Emails"),
                        "icon": "email",
                        "link": "/admin/account/emailaddress",
                    },
                    {
                        "title": _("Groups"),
                        "icon": "security",
                        "link": reverse_lazy("admin:auth_group_changelist"),
                    },
                ],
            },
            {
                "separator": True,
                "collapsible": False,
                "items": [
                    {
                        "title": _("OAuth Apps"),
                        "icon": "group",
                        "link": "/admin/socialaccount/socialaccount/",
                    }
                ],
            },
            {
                "separator": True,
                "collapsible": False,
                "items": [
                    {
                        "title": _("Audit Log"),
                        "icon": "timeline",
                        "link": "/admin/easyaudit/crudevent/",
                    }
                ],
            },
        ],
    },
    "TABS": [
        {
            "models": [
                "easyaudit.loginevent",
                "easyaudit.requestevent",
                "easyaudit.crudevent",
            ],
            "items": [
                {
                    "title": _("Crud Events"),
                    "link": "/admin/easyaudit/crudevent/",
                },
                {
                    "title": _("Login Events"),
                    "link": "/admin/easyaudit/loginevent/",
                },
                {
                    "title": _("Request Events"),
                    "link": "/admin/easyaudit/requestevent/",
                },
            ],
        },
        {
            "models": [
                "socialaccount.socialaccount",
                "socialaccount.socialapp",
                "socialaccount.socialtoken",
            ],
            "items": [
                {
                    "title": _("Social Account"),
                    "link": "/admin/socialaccount/socialaccount/",
                },
                {
                    "title": _("Social Token"),
                    "link": "/admin/socialaccount/socialtoken/",
                },
                {
                    "title": _("Social App"),
                    "link": "/admin/socialaccount/socialapp/",
                },
            ],
        },
    ],
}
