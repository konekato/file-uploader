from django.contrib import admin
from django.urls import include, path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('uploads/', include('app.urls'))
]
