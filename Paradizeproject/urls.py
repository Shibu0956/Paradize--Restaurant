"""
URL configuration for Paradizeproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ParadizeApp import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homepage),
    path('demohomepage/',views.demo_view),
    path('homepage/',views.homepage),
    path('masterfile/',views.master_view),
    path('userlogin/',views.login),
    path('usersign/',views.sign),
    path('logout/',views.logout),
    path('about/',views.About_View),
    path('offers/',views.Offer_View),
    path('contact/',views.Contact_View),
    path('orders/',views.Order_View),
    path('orderconfirm/',views.Order_confirm),
    # --- table urls ---
    path('mytable/',views.mytable),
    path('bookingConfirm/<int:formid>',views.bookingConfirm,name="bookingConfirm"),
    path('tabledit/<int:formid>',views.tabledit,name="tabledit"),
    path('tableupdate/<int:formid>',views.tableupdate,name="tableupdate"),
    path('TableBooked/<int:formid>',views.TableBooked_view,name="TableBooked_view"),
    path('TableSuccess/<int:formid>',views.TableSuccess_View,name="TableSuccess_View"),


    # --- table urls ---

     # --- menu urls ---
    path('menulist/',views.menu_list,name='menu_list'),
    path('foodcart/', views.view_cart, name='view_cart'),
    path('add/<int:product_id>/',views.add_to_cart,name='add_to_cart'),
    path('remove/<int:item_id>/',views.remove_from_cart,name='remove_from_cart'),
    path('Confirm_order/<int:product_id>/',views.Confirm_order_view,name="Confirm_order_view"),

    # --- table urls ---

     path('myorder/',views.order),

   

]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

