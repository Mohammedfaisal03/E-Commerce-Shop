from django.shortcuts import render,redirect,HttpResponse
from .models import Contact
from django.conf import settings
from django.core.mail import send_mail
from django.core.mail.message import EmailMessage
from django.core import mail
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages

# Create your views here.

def viewhome(request):
    return render(request,'projects/home.html')

def viewshop(request):
    return render(request,'projects/furni-shop.html')

def viewabout(request):
    return render(request,'projects/about-furni.html')

def viewservices(request):
    return render(request,'projects/furni-services.html')

def viewcontact(request):
    if request.method=='POST':
        fname=request.POST.get('first_name')
        lname=request.POST.get('last_name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        query=Contact(user_first_name=fname,user_last_name=lname,user_email=email,user_message=message)
        query.save()

        from_email=settings.EMAIL_HOST_USER
        connection=mail.get_connection()
        connection.open()
        # email_message=mail.EmailMessage(f'Eamil from {fname}')
        email_client=mail.EmailMessage(f" Furniture's Admin response",f'Thanks for reaching us\n\n Query: {message}',from_email,[email],connection=connection)

        connection.send_messages([email_client])
        connection.close()
        
        return redirect('home')

    return render(request,'projects/furni-contact.html')

def viewloginregister(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        
        try:
            user=User.objects.get(username=username)
        except:
            print('username does not exist ')

        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            print('user or password is incorrect')

        
    return render(request,'projects/login-register.html')

def viewlogout(request):
    logout(request)
    return redirect('login')


def viewregister(request):
    page='register'
    if request.method=="POST":
        u_username=request.POST.get('username')
        u_email=request.POST.get('email')
        u_password=request.POST.get('password')
        uc_password=request.POST.get('confirm_password')
        if u_password!=uc_password:
            messages.warning(request,'password is incorrect')
            return redirect('register')
        
        try:
            if User.objects.get(username=u_username):
                messages.info(request,'username is taken')
                return redirect('register')
        except:
            pass
        
        try:
            if User.objects.get(email=u_email):
                messages.warning(request,'email is existed')
                return redirect('register')
        except:
            pass

        query=User.objects.create_user(u_username,u_email,u_password)
        query.save()
        return redirect('login')

    return render(request,'projects/furni-register.html')

