from django.shortcuts import render, redirect, get_object_or_404
from .models import CleaningService, Booking
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import CustomerRegistrationForm, BookingForm

def home(request):
    return render(request,"main/home.html") 


@login_required(login_url='login')
def book_now(request):
    welcome_message = f"Welcome, {request.user.username}!"
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            cleaning_service = form.cleaned_data['cleaning_service']
            date = form.cleaned_data['date']
            time = form.cleaned_data['time']
            duration = form.cleaned_data['duration']
            customer = request.user.username

            B = Booking(
                customer=request.user,
                cleaning_service=cleaning_service,
                date=date,
                time=time,
                duration=duration
            )
            B.save()
            return redirect('booking_complete', booking_id=B.id)
    else:
        form = BookingForm()
    cleaning_service = CleaningService.objects.all()  # Fetch cleaning service queryset
    return render(request, 'main/book.html', {'form': form, 'welcome_message': welcome_message, 'cleaning_service': cleaning_service})

def about(request):
    return render(request,"main/about.html") 


def contact(request):
    return render(request,"main/contact.html") 



def register(request):
    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()   
            return redirect("login")
    else:
        form = CustomerRegistrationForm()

    return render(request, 'main/register.html', {'form': form})
   

def booking_complete(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    customer = booking.customer
    email = customer.email
    name = customer.username


    date = booking.date
    time = booking.time
    duration = booking.duration
    cleaning_service = booking.cleaning_service
    price = cleaning_service.price

   
    total_amount = float(duration) * float(price)
   

    return render(request, 'main/booking_complete.html', {
        'name': name,
        'email': email,
        'date': date,
        'time': time,
        'duration': duration,
        'cleaning_service': cleaning_service,
        'price': price,
        'total_amount': total_amount,
    })

