from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib import admin
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('', include(('common.urls', 'common'))),
    path(settings.ADMIN_URL, admin.site.urls),
    path('games/', include(('games.urls', 'games'))),
    path('docs/', include_docs_urls(title='My API service'), name='api-docs'),
    path('accounts/', include('allauth.urls')),
    # API urls
    path('api/v1/', include(([
        path('', include(('users.urls', 'users'))),
        path('', include(('flatpages.urls', 'flatpages'))),
        path('', include(('files.urls', 'files'))),
        path('', include(('games.api_urls', 'games')))
        # Your stuff: custom urls includes go here
    ], 'api'), namespace='api')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG and 'debug_toolbar' in settings.INSTALLED_APPS:
    import debug_toolbar
    urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns

# Admin Site Config
# https://docs.djangoproject.com/en/2.2/ref/contrib/admin/#adminsite-attributes
admin.sites.AdminSite.site_header = settings.ADMIN_SITE_HEADER
admin.sites.AdminSite.site_title = settings.ADMIN_SITE_TITLE
