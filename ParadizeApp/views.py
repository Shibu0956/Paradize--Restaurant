from django.shortcuts import render,redirect
from ParadizeApp.models import userlogin,usersign,Chefs,Foodmenu,FoodCart,Review,OrderMenu,Booking_Table,About,Offer,myCarousel
from django.http import HttpResponse
from ParadizeApp.form import userform,userform1,tableform
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
def demo_view(request):
      return render(request,'demohomepage.html')

def master_view(request):
      return render(request,'masterfile.html')

def homepage(request):
      home = userlogin.objects.all()
      mycarousel= myCarousel.objects.all()
      cheif=Chefs.objects.all()
      table = tableform(request.POST)
      menu = Foodmenu.objects.all()
      review = Review.objects.all()
      context={
            "home":home,
            "mycarousel":mycarousel,
            "cheif":cheif,
            "table" :table,
            "menu" : menu,
            "review" :review,
            
      }
      return render(request,'homepage.html',context)

def order(request):
      home = userlogin.objects.all()
      return render(request,'order.html')
    
def sign(request):
      form = userform1(request.POST)
      if request.method == "POST":
            Email = request.POST.get('Email')
            Username = request.POST.get('Username')
            Password = request.POST.get('Password')
            if  usersign.objects.filter(Username=Username).count()>0:
                  messages.info(request,"Username already exists.")    

            elif usersign.objects.filter(Email=Email).count()>0:
                 messages.info(request,"Email already exists.")

            else:  
                  # form.is_valid(): 
                  try:
                      form.save()
                      return redirect('/userlogin')
                  except:
                        pass
                  
      else:
            form = userform1()
            # return redirect('/usersign')
      return render(request,'usersign.html')   
  
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

# ===== table_view ======= #

def mytable(request):
      if request.method == "POST":
            print("Form Submitted")
            table = tableform(request.POST)
            print("enter inside")
            if table.is_valid():
                  formdata = table.save()
                  print("Form data saved:",formdata.id)
                  return redirect('bookingConfirm',formid=formdata.id)
      else:
            table=tableform()
            print("not saved")
      return render(request,'mytable.html',{'table':table})      


def bookingConfirm(request,formid):
      table = Booking_Table.objects.get(id=formid) 
      if request.method =="POST":
              return redirect('tabledit',formid=formid)
      context ={
            'table':table
      }
      return render(request,'booktable.html',context)

def tabledit(request,formid):
      table = Booking_Table.objects.get(id=formid)
      print(table) 
      # if request.method =="POST":
      #         return redirect('tableupdate',formid=formid)
      context ={
            'table':table
      } 
      
      return render(request,'tabledit.html',context)

def tableupdate(request,formid):
      table = Booking_Table.objects.get(id=formid)
      context = {
            'table':table
      }
      table1 = tableform(request.POST,instance=table)
      if table1.is_valid():
            print("form updated")
            table1.save()
            return redirect("bookingConfirm",formid=formid)
      return render(request,'tabledit.html',context)

      # print(table)   
      # table1 = tableform(request.POST)
      # print(table1)   
      # # messages.info("table not valid")
     
      # if table1.is_valid():
      #       print("form updated")
      #       table1.save()
      #       return redirect("TableBooked_view",formid=formid)
      # else:
      #       tableform()
      #       print("form not updated")
      # return render(request,"tabledit.html",{'table':table})

def TableBooked_view(request,formid):
      table = Booking_Table.objects.get(id=formid)   
      context={
            'table':table
      }
      return render(request,'TableBooked.html',context)


# ===== table_view ======= #
            
# ===== menu_view ======= #
def menu_list(request):
      menu=Foodmenu.objects.all()
      context ={
            'menu':menu
      }
      return render(request,'Foodmenulist.html',context)

def view_cart(request):
      cart_items = FoodCart.objects.filter(user=request.user)
      total_price = sum(item.product.Price * item.quantity for item in cart_items)
      context ={
            'cart_items':cart_items,
            'total_price':total_price
      }
      return render(request, 'FoodmenuCart.html',context)

def add_to_cart(request,product_id):
      product = Foodmenu.objects.get(id=product_id)
      cart_item, created = FoodCart.objects.get_or_create(product=product,user=request.user)
      cart_item.quantity += 1
      cart_item.save()
      return redirect('view_cart')

def remove_from_cart(request, item_id):
	cart_item = FoodCart.objects.get(id=item_id)
	cart_item.delete()
	return redirect('view_cart')

def orderMenu(request,id):
      menu = Foodmenu.objects.get(id=id)
      context ={
            'menu':menu,
      }
      return render(request,'menuOrder.html',context)

# ===== menu_view ======= #

def About_View(request):
      about = About.objects.all()
      context = {
            'about':about
      }
      return render(request,'about.html',context)

def Offer_View(request):
      offer = Offer.objects.all()
      context = {
            'offer':offer
      }
      return render(request,'offers.html',context)

def Contact_View(request):
      return render(request,'contact.html')

def Order_View(request):
      return render(request,'orders.html')
             
def Order_confirm(request):
      return render(request,'order.html')

