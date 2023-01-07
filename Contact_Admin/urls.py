from django.contrib import admin
from django.urls import path
from Contact_Admin import views
from django.conf.urls.static import static
from django.conf import settings

app_name = "Contact_Admin"

urlpatterns = [
    path('', views.Sent_downloadable_link, name='Sent_downloadable_link')
]