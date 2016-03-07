from django.conf.urls import url, include
from django.contrib import admin
from apps.panel import urls as panel_urls

urlpatterns = [
	url(r'^', include(panel_urls, 'panel_app')),
	url(r'^admin/', admin.site.urls),
]
