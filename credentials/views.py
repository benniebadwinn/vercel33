from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
# Create your views here.
# 

def login (request):
     if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        User = auth.authenticate(username=username, password=password)

        if User is not None:
               auth.login(request, User)
               return redirect("/")
    
        else:
            messages.info(request, 'Wrong Password Or Username')
            return render (request, 'login.html')  

     else:
      return render(request, 'login.html')

def register (request):

    if request.method == 'POST':
       
       first_name = request.POST['first_name']
       last_name = request.POST['last_name']
       username = request.POST['username']
       email = request.POST['email']
       password1 = request.POST['password1']
       password2 = request.POST['password2']

       if password1==password2:
         if User.objects.filter(email=email).exists():
             messages.info(request, 'Email Already Exist Try Another One')
             return redirect('register')
         elif User.objects.filter(username=username).exists():
                 messages.info(request, 'Username Already Exist!!! Try Another One')
                 return redirect('register')
         else:
     
            user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email,)
            user.save()
            messages.info(request, 'Your Account Has Been Succesfully Created')
            return redirect('login')
            
       else:
        messages.info(request, 'Password Do Not Match...')
        return redirect('register')
        return redirect('/')

    else:
        return render(request, 'register.html')


def logout (request):
            auth.logout(request)
            return redirect('/')