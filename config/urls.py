from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.urls import include, path
from debug_toolbar.toolbar import debug_toolbar_urls


# urlpatterns = (
#     [
#         path("i18n/", include("django.conf.urls.i18n")),
#     ]
#     + i18n_patterns(
#         path("admin/", admin.site.urls),
#         path("__reload__/", include("django_browser_reload.urls")),
#     )
#     + debug_toolbar_urls()
#     + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT),
# )


urlpatterns = (
    [
        path("i18n/", include("django.conf.urls.i18n")),
    ]
    + i18n_patterns(
        path("", include("core.urls")),
        path("admin/", admin.site.urls),
        path("__reload__/", include("django_browser_reload.urls")),
        path("accounts/", include("allauth.urls")),
    )
    + debug_toolbar_urls()
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
)
