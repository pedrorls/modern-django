from django.conf.urls import , include
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('project.api.urls')),
]
