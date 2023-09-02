from django.urls import path
from . import views
urlpatterns = [
    path('product',views.product),
    path('contact',views.contact),
    path('blog',views.blog),
    path('home-02',views.home),
    path('home-03',views.homes),
    path('shoping-cart',views.shoping),
    path('about',views.about),
    path('',views.indexs,name='index'),
    path('admineform',views.admineform),
    path('signup',views.index),
    path('login',views.userlogin),
    path('logout',views.userlogout),
    path('viewdetail',views.viewdetail,name='viewdetail'), 
    path('kkk',views.kkk),   
    path('iitem',views.iitem),
    path('wished',views.wished),
    path('userwish',views.userwish),
    path('userwishlist',views.userwishlist),
    path('cart_info',views.cart_info),
    path('cart_view',views.cart_view),
    path('view_cart_details/<int:id>',views.view_cart_details,name='view_cart_details'),
    path('checkoutdetail',views.checkoutdetail),

]

