from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class userlogin(models.Model):
    Username = models.CharField(max_length=100,unique =True)
    Password = models.CharField(max_length=100)

    class Meta:
        db_table = "userlogin"

class usersign(models.Model):
    Fullname = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Username = models.CharField(max_length=100,unique =True)
    Password = models.CharField(max_length=100)

    class Meta:
        db_table = "usersign"

class About(models.Model):
    Image = models.ImageField()
    class Meta:
        db_table = "About"


class Chefs(models.Model):
    Image =models.ImageField()
    Name = models.CharField(max_length=50) 
    Designation = models.CharField(max_length=50) 
    Content = models.CharField(max_length=250) 
    class Meta:
        db_table ="Chefs"

class Foodmenu(models.Model):
    Image =models.ImageField()
    Name = models.CharField(max_length=50)
    Description = models.CharField(max_length=50,null=True)
    Price = models.DecimalField(max_digits=5, decimal_places=2,null=True)
    
    def __str__(self):
        return self.Name    

class FoodCart(models.Model):
    product = models.ForeignKey(Foodmenu, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.quantity} x {self.product.Name}'

class Review(models.Model):
    Image = models.ImageField()
    Content = models.CharField(max_length=550)
    class Meta:
        db_table = "Review"   


class Order(models.Model):
    Decription = models.CharField(max_length=50)
    Qty = models.IntegerField(default=0)
    Price = models.DecimalField(max_digits=5, decimal_places=2)
    Total_Amount = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        db_table = "Order"          

class OrderMenu(models.Model):
    Description = models.ImageField()
    Name = models.CharField(max_length=50,null=True)
    Qty = models.IntegerField(default=0)
    Price = models.DecimalField(max_digits=5, decimal_places=2)
    Total_Amount = models.DecimalField(max_digits=5, decimal_places=2)
    class Meta:
        db_table = "OrderMenu"  
        
class demoorder(models.Model):
    Name = models.CharField(max_length=50)
    Age = models.IntegerField()
    class Meta:
        db_table = "demo"  

class Booking_Table(models.Model):
    Name = models.CharField(max_length=50)   
    Phone_No =  models.IntegerField() 
    Email = models.CharField(max_length=50) 
    Person_nos = models.IntegerField() 
    Date = models.DateField(blank=True, null=True)
    Time = models.TimeField(blank=True, null=True)
    Message = models.CharField(max_length=250,null=True)   
    class Meta :
        db_table = "BookingTable"
        

class Offer(models.Model):
    Image = models.ImageField()
    class Meta:
        db_table = "Offer"

class myCarousel(models.Model):
    Image = models.ImageField()
    Content = models.CharField(max_length=50) 
    class Meta:
        db_table = "myCarousel"
