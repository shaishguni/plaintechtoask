from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from Main import urls
import os
from Project.settings import BASE_DIR

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include(urls))
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR),"static_cdn")	


admin.site.site_header = "Tech To Ask"
admin.site.site_title = "Tech Group.inc"
admin.site.index_title = "Welcome to the admin page."
