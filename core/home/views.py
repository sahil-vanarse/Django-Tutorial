from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'index.html')

def success_page(request):
    return HttpResponse("Hey this is a response page")