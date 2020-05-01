from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_details, name='upload_details'),
]
