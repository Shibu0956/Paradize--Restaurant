from django.contrib import admin
from ParadizeApp.models import usersign,About,Chefs,Foodmenu,FoodCart,Review,OrderMenu,demoorder,Booking_Table,Offer,myCarousel,FoodCart

# Register your models here.
class UsersignAdmin(admin.ModelAdmin):
    list_display=("Fullname","Email","Username","Password",)
admin.site.register(usersign,UsersignAdmin)

class AboutAdmin(admin.ModelAdmin):
    list_display = ('Image',)
admin.site.register(About,AboutAdmin)    

class ChefsAdmin(admin.ModelAdmin):
    list_display = ("Image","Name","Designation","Content",)
admin.site.register(Chefs,ChefsAdmin)  

admin.site.register(Foodmenu)
admin.site.register(FoodCart)
# class MenuAdmin(admin.ModelAdmin):
#     list_display = ('Image','Description','Qty','Price','Total_Amount',)
#     list_editable = ('Total_Amount'),
# admin.site.register(Foodmenu,MenuAdmin)

# class FoodcartAdmin(admin.ModelAdmin):
#     list_display=('product','qty','user','data_added',)
# admin.site.register(FoodCart,FoodcartAdmin)

class ReviewAdmin(admin.ModelAdmin):
    list_display=('Image','Content',)
admin.site.register(Review,ReviewAdmin) 

class OrderMenuAdmin(admin.ModelAdmin):
    list_display = ('Description','Name','Qty','Price','Total_Amount',)
admin.site.register(OrderMenu,OrderMenuAdmin)    

class demoadmin(admin.ModelAdmin):
    list_display = ('Name','Age',)
admin.site.register(demoorder,demoadmin)

class Booking_Table_Admin(admin.ModelAdmin):
    list_display = ('Name','Phone_No','Email','Person_nos','Date','Time','Message',)
    list_editable = ('Email'),
admin.site.register(Booking_Table,Booking_Table_Admin)

class OfferAdmin(admin.ModelAdmin):
    list_display = ('Image'),
admin.site.register(Offer,OfferAdmin)

class CarouselAdmin(admin.ModelAdmin):
    list_display = ('Image','Content',)
    list_display_links=['Image']
admin.site.register(myCarousel,CarouselAdmin)
  
  