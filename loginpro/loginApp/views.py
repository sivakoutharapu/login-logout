from django.shortcuts import render,redirect,HttpResponse
from .models import covid_data
from django.contrib.auth import login as auth_login,logout,authenticate
from django.contrib.auth.models import User
# Create your views here.

def register_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        if not username:
            return render(request, 'register.html', {'error': 'username not available'})
        
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        return redirect('login_user')
    
    return render(request, 'register.html')


def home_page(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        carona_status = request.POST.get('carona_status')
        place = request.POST.get('place')
        
        carona_details = covid_data(name=name, age=age, carona_status=carona_status, place=place)
        carona_details.save()
    data = covid_data.objects.all()
    return render(request,'index.html', {'data':data})

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth_login(request, user)
            return redirect('home_page')
        else:
            return render(request,'login.html')
    return render(request,'login.html')

def logout_user(request):
    logout(request)
    return redirect('login_user')