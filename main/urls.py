from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('book_now/', views.book_now, name='book_now'),
    path('register/', views.register, name='register'),
    path('booking_complete/<int:booking_id>/', views.booking_complete, name='booking_complete')

    
]
