from django.contrib import admin
from django.urls import path
from core import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('rent/', views.rent_trailer, name='rent_trailer'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('driver_dashboard/', views.driver_dashboard, name='driver_dashboard'),
    path('renter_dashboard/', views.renter_dashboard, name='renter_dashboard'),
    path('test/', views.test, name='test'),
]
