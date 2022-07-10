from django.shortcuts import get_object_or_404, redirect, render
from django.core.mail import send_mail

def index(request):
    return render(request, 'index.html')

def what_we_do(request):
    return render(request, 'what_we_do.html')

def reviews(request):
    return render(request, 'reviews.html')

def booking(request):
    
    if request.method == "POST":
        booking_name = request.POST['booking-name']
        booking_email = request.POST['booking-email']
        booking_reason = request.POST['booking-reason']
        
        message = "Email: " + booking_email + "\n" + "Reason: "+ booking_reason
        send_mail(
            "Session Request: " + booking_name, 
            message,
            booking_email,
            ['nicholas.kissaun@gmail.com']
        )
        
        return render(request, 'booking.html', {"booking_name": booking_name})
    else:      
        return render(request, 'booking.html', {})