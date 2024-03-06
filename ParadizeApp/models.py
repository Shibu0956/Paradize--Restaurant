from django.db import models

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


class Order(models.Model):
    Decription = models.CharField(max_length=50)
    Qty = models.IntegerField(default=0)
    Price = models.DecimalField(max_digits=5, decimal_places=2)
    Total_Amount = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        db_table = "Order"