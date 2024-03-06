from django.shortcuts import render,redirect
from ParadizeApp.models import userlogin,usersign
from django.http import HttpResponse
from ParadizeApp.form import userform,userform1
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
# def loginpage(request):
#       home = userlogin.objects.all()
#       return render(request,'login.html')

# def demosign(request):
#       home = userlogin.objects.all()
#       return render(request,'demosig.html')

def homepage(request):
      home = userlogin.objects.all()
      return render(request,'homepage.html')

def order(request):
      home = userlogin.objects.all()
      return render(request,'order.html')
    
def sign(request):
      form = userform1(request.POST)
      if request.method == "POST":
  
            Email = request.POST.get('Email')
            Username = request.POST.get('Username')
            Password = request.POST.get('Password')
            if form.is_valid():
                    try:
                      form.save()
                      return redirect('/userlogin')
                    except:
                        pass
      else:
            form = userform1()
            # return redirect('/usersign')
      return render(request,'usersign.html')   

            # if    usersign.objects.filter(Email=Email).count()>0:
            #       messages.info(request,"Email already exists.")

            # elif  usersign.objects.filter(Username=Username).count()>0:
            #       messages.info(request,"Username already exists.")    

            # else:   

def demosign(request):
     return render(request,"usersign.html")
  
def login(request):
      form = userform(request.POST)
      if request.method == "POST":   
         Username = request.POST.get('Username')
         Password = request.POST.get('Password')
         check_user = usersign.objects.filter(Username=Username,Password=Password)
         if check_user:

            return redirect('/homepage')
                  
         else: 
                 form = userform()
                 messages.info(request,"Enter valid username or password")
      return render(request,'userlogin.html')           

def logout(request):
	  return redirect('login')

def mymenu(request):
      home1 = userlogin.objects.all()
      return render(request,'menu.html')





             


