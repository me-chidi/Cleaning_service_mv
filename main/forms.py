from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,authenticate
from django.contrib.auth.models import User
from .models import CleaningService,Booking


class CustomerRegistrationForm(UserCreationForm):
    address = forms.CharField(max_length=255, required=True)
    phone_number = forms.CharField(max_length=15, required=True)


    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number','address','password1', 'password2']



class BookingForm(forms.ModelForm):
    name = forms.CharField(max_length=255, required=True)
    address = forms.CharField(max_length=255, required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = Booking
        fields = ['name', 'address', 'email',  'cleaning_service', 'date', 'time', 'duration']

