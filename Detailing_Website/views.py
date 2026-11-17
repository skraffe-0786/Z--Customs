from django.shortcuts import render, redirect
from django.contrib import messages

from .form import ContactFrom

from .models import Booking
from datetime import date
from django.utils import timezone

# Create your views here.
def HomePage(request):
    return render(request, "Home.html")
def Service_Page(request):
    return render(request,"services.html")
def Contact_Page(request):

    if request.method == 'POST':
        form = ContactFrom(request.POST)

        if form.is_valid():
            contact = form.save()

            print("\n========= NEW CUSTOMER ENQUIRY =========")
            print("Name :", contact.name)
            print("Email :",contact.email)
            print("Phone :",contact.phone)
            print("Service :",contact.service)
            print("Message :",contact.message)
            print("===========================================")
            
            messages.success(request, "Your message has been submitted successfully!")
            return redirect('contact')

    else:
        form = ContactFrom()

    return render(request, "Contact.html", {"form": form})

def BookNow(request):
    if request.method == 'POST':

        full_name = request.POST.get('full_name', '').strip()
        email = request.POST.get('email', '').strip()
        phone = request.POST.get('phone', '').strip()
        vehicle = request.POST.get('vehicle', '')
        service = request.POST.get('service', '')
        booking_date = request.POST.get('date', '')
        booking_time = request.POST.get('time', '')
        booking_message = request.POST.get('message', '').strip()

        # Check required fields
        if not all([
            full_name, email, phone, vehicle,
            service, booking_date, booking_time
        ]):
            messages.error(request, "Please fill in all required fields.")
            return redirect('BookNow')

        try:
            selected_date = date.fromisoformat(booking_date)

            if selected_date < timezone.localdate():
                messages.error(request, "Please select a valid future date.")
                return redirect('BookNow')

            if vehicle not in ['Car', 'Bike']:
                raise ValueError()

            valid_services = [
                choice[0] for choice in Booking.SERVICE_CHOICES
            ]

            if service not in valid_services:
                raise ValueError()

            Booking.objects.create(
                full_name=full_name,
                email=email,
                phone=phone,
                vehicle=vehicle,
                service=service,
                date=selected_date,
                time=booking_time,
                message=booking_message
            )
            print("\n=========NEW BOOKING DETAILS==============")
            print("Name :",full_name)
            print("Email :",email)
            print("Phone :",phone)
            print("vehicle :",vehicle)
            print("Service :",service)
            print('date :',selected_date)
            print('time :',booking_time)
            print("Message :",booking_message)
            print("\n===========================================")

            messages.success(
                request,
                'Your appointment request has been submitted successfully!'
            )

            return redirect('BookNow')

        except ValueError:
            messages.error(request, "Please enter valid booking details.")
            return redirect('BookNow')

    return render(request, "Booknow.html")


def ourwork(request):
    return render(request, "OurWork.html")

def ourwork(request):
    return render(request,"OurWork.html")