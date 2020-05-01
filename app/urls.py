from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_details, name='upload_details'),
    path('<int:detail_id>/', views.upload_file, name='upload_file')
]
