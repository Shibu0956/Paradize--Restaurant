from django import forms
from ParadizeApp.models import userlogin,usersign,Order

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