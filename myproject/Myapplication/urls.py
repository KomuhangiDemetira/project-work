from django.urls import path

#let us reuse the django login view.
from django.contrib.auth import views as auth_views
from Myapplication import views

urlpatterns = [
    #path('index/',views.index, name='index'),
    path('',views.index, name='index'),
    path('home', views.home, name='home'),
    path('home/<int:product_id>', views.product_detail, name='prduct_detail'), 

    path('login/', auth_views.LoginView.as_view(template_name = 'Demi/login.html'), name= 'login'),


    path('receipt/', views.receipt, name='receipt'),
    path('receipt_detail/<int:receipt_id>', views.receipt_detail, name='receipt_detail'),
     
    
    path('issue_item/<str:pk>',views.issue_item, name = 'issue_item'),
    path('home/<int:product_id>',views.product_detail, name ='product_detail'),
    path('made_sales/', views.made_sales, name='made_sales'),
    path('add_to_stock/<str:pk>', views.add_to_stock, name='add_to_stock'),
    
    #path('login/',auth_views.LoginView.as_view(template_name='Demi/login.html'), name ='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='Demi/index.html'), name ='logout'),
]   
