from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from events.models import events
# from django.core.mail import send_mail
from .models import events, Booking
from  .forms import BookingForm
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def home_page(request):
    return render(request,'home_page.html')


def product_add(request):
    obj=events.objects.all()
    return render(request,'product_add.html',{'x':obj})


    
    

def user_log(request):
    if request.method=='POST':
        username=request.POST.get('u1')
        password=request.POST.get('p1')
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/login_page/')
    return render(request,'login_page.html')



def book_event(request):
    if request.method == 'POST':
        name = request.POST.get('v1')
        email = request.POST.get('k1')
        booked_at = request.POST.get('o1')
        
        # Assuming you have a model named Booking to store the event bookings
        # Create a new booking instance and save it to the database
        new_booking = Booking( name=name, email=email, booked_at=booked_at)
        new_booking.save()
        
        # Optionally, you can send a confirmation email to the user here
        
    return render(request, 'booking_page.html')



    # event = events.objects.get(id=pk)
    # if request.method == 'POST':
    #     form = BookingForm(request.POST)
    #     if form.is_valid():
    #         booking = form.save(commit=False)
    #         booking.event = event
    #         booking.save()
    #         # send_confirmation_email(booking)
    #         return product_add(request)
    # else:
    #     form = BookingForm()
    # return render(request, 'prpduct_add.html', {'form': form})

# def send_confirmation_email(booking):
#     subject = 'Confirmation: Event Booking'
#     message = f'Hi {booking.name},\nThank you for booking {booking.event.name} on {booking.event.date}.'
#     send_mail(subject, message, 'from@example.com', [booking.email])


