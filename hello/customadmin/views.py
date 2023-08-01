from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,get_user_model,logout,login
from django.contrib import messages

# Create your views here.
def admin_login(request):
    if request.method=="POST":
        username=request.POST.get('userr')
        password=request.POST.get('pass')
        user=authenticate(request,username=username,password=password)
        if user is not None and user.is_staff:
            return redirect('admin_dashboard/')
        else:
            messages.warning(request, 'username or Password does not match')
            return redirect('/login')
    return render(request,'login.html')
        