from django.shortcuts import *
from django.http import *
from vege.models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='/login/')
def receipes(request):
    if request.method == "POST":
        data = request.POST
        receipeName = data.get('receipe_name')
        receipeDes = data.get('receipe_description')
        receipeImage = request.FILES.get('receipe_image')
        
        receipe = Receipe(
            receipe_name=receipeName,
            receipe_description=receipeDes,
            receipe_image=receipeImage
        )
        receipe.save()
        
        return redirect('/receipes')
    
    querySet = Receipe.objects.all()

    if request.GET.get('search_receipe'):
        querySet = querySet.filter(receipe_name__icontains=request.GET.get('search_receipe'))

    context = {'receipes': querySet}
        
    return render(request, "receipe.html", context)

@login_required(login_url='/login/')
def delete_receipe(request, id):
    querySet = Receipe.objects.get(id=id)
    querySet.delete()
    return redirect('/receipes')

@login_required(login_url='/login/')
def update_receipe(request, id):
    querySet = Receipe.objects.get(id=id)
    if request.method == "POST":
        updated_receipe_name = request.POST.get('receipe_name')
        updated_receipe_description = request.POST.get('receipe_description')
        updated_receipe_image = request.FILES.get('receipe_image')

        querySet.receipe_name = updated_receipe_name
        querySet.receipe_description = updated_receipe_description

        if updated_receipe_image:
            querySet.receipe_image = updated_receipe_image

        querySet.save()
        return redirect('/receipes')

    context = {'receipe': querySet}
    return render(request, "update_receipe.html", context)

def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Debugging statements
        print(f"Trying to authenticate user: {username}")

        if not User.objects.filter(username=username).exists():
            messages.error(request, 'Invalid username')
            print(f"User {username} does not exist")
            return redirect('/login/')

        user = authenticate(username=username, password=password)

        if user is None:
            messages.error(request, 'Invalid Credentials')
            print(f"Authentication failed for user: {username}")
            return redirect('/login/')
        else:
            login(request, user)
            print(f"User {username} authenticated successfully")
            return redirect('/receipes/')
    return render(request, 'login.html')

def register_page(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        userexist = User.objects.filter(username=username)
        if userexist.exists():
            messages.info(request, 'Username already exists')
            return redirect('/register/')

        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username
        )

        user.set_password(password)
        user.save()
        messages.info(request, 'Account created successfully')
        return redirect('/register/')
    return render(request, 'register.html')


@login_required(login_url='/login/')
def logout_page(request):
    logout(request)
    return redirect('/login/')