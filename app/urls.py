from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('uploads/', views.upload_details, name='upload_details')
]
