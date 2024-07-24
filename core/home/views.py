from django.shortcuts import * # type: ignore
from django.http import HttpResponse # type: ignore
from home.models import Car
from vege.seed import *
from .utils import send_email_to_client, send_email_with_attachment
from django.conf import settings
import os

def send_email(request):
    subject = "This is the email with the attachment"
    message = "I hope you have clear understanding of the Django Mail now"
    receipients_list = ['sahilvanarse4@gmail.com', 'sahilvanarse23@gmail.com']
    file_path = os.path.join(settings.BASE_DIR, 'main.xlsx')

    send_email_with_attachment(subject, message, receipients_list, file_path)
    return redirect('/')

def home(request):
    # seed_db(100)
    Car.objects.create(car_name = f"Nexon-{random.randint(0, 100)}")
    people = [
        {'name' : 'Sahil Vanarse', 'age' : 22},
        {'name' : 'Deepen Vanarse', 'age' : 25},
        {'name' : 'Kunal Jadhav', 'age' : 16},
    ]

    text = "Hello Guys I m Learning Django and it is intresting"

    vegetables = ['tomato', 'cucumber', 'cabbage']
    return render(request, 'index.html', context = {'page' : 'Django','people' : people, 'text' : text, 'vegetables' : vegetables})

def success_page(request):
    return HttpResponse("Hey this is a response page")

def about(request):
    context = {'page' : 'About'}
    return render(request, 'about.html', context)


def contact(request):
    context = {'page' : 'Contact'}
    return render(request, 'contact.html', context)