from django import forms
import datetime

from ParadizeApp.models import userlogin,usersign,Order,Chefs,Foodmenu,Booking_Table,OrderMenu,FoodCart
from django.contrib.admin.widgets import AdminDateWidget,AdminTimeWidget
# from Paradizeproject.settings import DATE_INPUT_FORMATS

class userform(forms.ModelForm):
    class Meta:
        model = userlogin
        fields = "__all__"
        

class userform1(forms.ModelForm):  
    class Meta:
        model = usersign
        fields = "__all__"  

class orderform(forms.ModelForm):  
    class Meta:
        model = Order
        fields = "__all__"   

class DateInput(forms.DateInput):
    input_type = 'date'
    

class tableform(forms.ModelForm):
    Name = forms.CharField (widget=forms.TextInput(attrs={'placeholder':'Your Name','class':'tablename'})) 
    Phone_No =  forms.CharField (widget=forms.TextInput(attrs={'placeholder':'Phone No','class':'tablename'}))
    Email = forms.CharField (widget=forms.TextInput(attrs={'placeholder':'Email','class':'tablename'}))  
    Person_nos = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'#No of Persons','class':'tablename'}))
    Date = forms.DateField(widget=AdminDateWidget(attrs={'type':'date','class':'dateclr'}))
    Time = forms.TimeField(widget=AdminTimeWidget(attrs={'type':'time','class':'timeclr'}))
    Message = forms.CharField(max_length=100,widget=forms.Textarea(attrs={'placeholder':'Message','class':'tarea',"rows":3, "cols":50,}))
    class Meta:
        model = Booking_Table
        fields = ['Name','Phone_No','Email','Person_nos','Date','Time','Message',]
        widgets = {
            'Date': AdminDateWidget(),
            'Time': AdminDateWidget(),

        }
        
class Chefsform(forms.ModelForm):
    Image = forms.ImageField()
    Name = forms.CharField (label="Name",max_length=50,) 
    Designation = forms.CharField (label="Designation",max_length=50,)
    Content = forms.CharField (label="Content",max_length=250,)
    class Meta:
            model = Chefs
            fields =['Image','Name','Designation','Content',]

# class Foodmenuform(forms.ModelForm):   
#     class Meta:
#         model = OrderMenu
#         fields = "__all__" 

class FootMenuForm(forms.ModelForm):
    class Meta:
        model = Foodmenu
        fields = "__all__"          

class FoodCartForm(forms.ModelForm):
    class Meta:
        model = FoodCart
        fields = "__all__" 
       