from django.shortcuts import render # type: ignore
from django.http import HttpResponse # type: ignore

def home(request):
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