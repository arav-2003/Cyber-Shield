from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm
from .models import User

from django.contrib.auth.hashers import make_password
from .kms_utils import KMSUtils
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate #, login


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            # Encrypt sensitive data before saving
            name = form.cleaned_data['name']
            dob = form.cleaned_data['dob']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            confirm_password =  form.cleaned_data['confirm_password']
            encrypted_password = KMSUtils.encrypt(form.cleaned_data['password'])
            #user.password = make_password(form.cleaned_data['password'])  # Encrypt the password
            User.password = encrypted_password
            #User.save()
            User.objects.create(name=name,dob = dob, phone_number=phone_number, email=email, password=encrypted_password , confirm_password= confirm_password).save()
            return redirect('success')  # Redirect to success page after registration
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def success(request):
    return render(request, 'success.html')

def login_success(request):
    return render(request, 'login_success.html')

def about(request):
    return render(request, 'about.html')

def welcome(request):
    return render(request, 'welcome.html')

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            login_email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            # Decrypt the stored password from the database
            user = User.objects.filter(email=login_email).first()
            
            if user:
                print ("login: ",type(user.password))
                decrypted_password = KMSUtils.decrypt(user.password)
                if decrypted_password == password:
                    # Passwords match, authenticate the user
                    print("Decrypted password:", (decrypted_password))
                    print("Provided password:", (password))
                    if(login_email==user.email and decrypted_password == password ):
                        return redirect('login_success')  # Redirect to success page
                else:
                    # Passwords don't match, display error message
                    return render(request, 'login.html', {'form': form, 'error': 'Invalid email or password.'})
            else:
                # User not found, display error message
                return render(request, 'login.html', {'form': form, 'error': 'User not found.'})
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

