from django.contrib import admin
from django.urls import path
from scoutapp import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.scout, name='scout'),
    path("landpage/", views.land, name='landpage')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
