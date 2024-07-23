from django.shortcuts import * # type: ignore
from django.http import HttpResponse # type: ignore
from vege.seed import *
from .utils import send_email_to_client

def send_email(request):
    send_email_to_client()
    return redirect('/')

def home(request):
    seed_db(100)
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