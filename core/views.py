from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .models import *
from .forms import RegisterAccountForm, ProfileCreationForm
# Create your views here.


@login_required(login_url='/login')
def homePage(request):
    return render(request, 'home-page.html')


def logoutPage(request):
    logout(request)
    messages.success(request, 'Logged out')
    return redirect('/?login=False&logout=True')

@login_required(login_url='/login')
def newProfilePage(request):
    if request.method == 'POST':
        try:
            form = ProfileCreationForm(request.POST or None)
            if form.is_valid():

                new_profile = profile.objects.create(
                    user = request.user,
                    full_name = form.cleaned_data.get('full_name'),
                    phone_no = form.cleaned_data.get('phone_no'),
                    gender = form.cleaned_data.get('gender'),
                    nationality = form.cleaned_data.get('nationality'),
                )

                if 'profession' in request.POST and request.POST['profession'] != '':
                    new_profile.profession = request.POST['profession']

                if 'place' in request.POST and request.POST['place'] != '':
                    new_profile.place = request.POST['place']

                if 'address' in request.POST and request.POST['address'] != '':
                    new_profile.address = request.POST['address']

                if len(request.FILES) != 0:
                    new_profile.img = request.FILES['img']          
                
                new_profile.save()
                messages.success(request, "Profile created")
                return redirect('/?login=True&account=True&profile=True')
            messages.error(request, "Fill all fields")
        except Exception as err:
            print(err)                  
    return render(request, 'new-profile.html')    

def registerPage(request):
    if request.method == 'POST':
        try:
            form = RegisterAccountForm(request.POST)
            if form.is_valid() and form.cleaned_data.get('password1') == form.cleaned_data.get('password2'):
                form.save()
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password1')
                user = authenticate(request, username=username, password=password)
                if user:
                    login(request, user)
                    messages.success(request, "Account created")
                    return redirect('/new/profile?login=True&account=True')
                messages.error(request, "Something went wrong")
            messages.error(request, "Fill all fields")
        except Exception as err:
            print(err)                  
    return render(request, 'register-page.html')           



@login_required(login_url='profile/')
def profilePage(request):
    if request.method == 'POST':
        try:
            if 'dfd' in request.POST and request.POST['dfd']:
                dfd = request.POST['dfd']
                
            messages.success(request, "Profile Updated")
        except Exception as err:
            print(err)    
    return render(request, "profile-page.html")




def loginPage(request):
    if request.method == 'POST':
        try:
            if 'username' in request.POST and 'password' in request.POST and request.POST['username'] != '' and request.POST['password'] != '':
                username = request.POST['username']
                password = request.POST['password']
                user = authenticate(username=username, password=password)
                if user:
                    login(request, user)
                    messages.success(request, "Login Successful")
                    if profile.objects.filter(user=request.user).exists():
                        return redirect('/?login=True&profile=True')
                    return redirect('/new/profile?login=True&profile=False')    
                messages.error(request, "Username and Password didn't match")
            messages.error(request, "Please provide Username and Password")
        except Exception as err:
            print(err)         
    return render(request, 'login-page.html') 