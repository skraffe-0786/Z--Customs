from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage, name='home'),
    path('services/', views.Service_Page, name='services'),
    path('contact/', views.Contact_Page, name='contact'),
    path('booknow/', views.BookNow, name='BookNow'),
    path('About/', views.About, name='ourwork'),
]