"""
URL configuration for Project_Ban_May_Tinh project.

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
from app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('checkout/', views.checkout, name='checkout'),
    path('detail-product/', views.detail_product, name='detail_product'),
    path('store/', views.store, name='store'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('forgot-password/', views.forgot_password, name='forgot_password'),
    # Admin
    path('home-manage/', views.home_manage, name='home_manage'),
    path('product-manage/', views.product_manage, name='product_manage'),
    path('order-manage/', views.order_manage, name='order_manage'),
    path('user-manage/', views.user_manage, name='user_manage'),
    path('logout/', views.logout_view, name='logout'),
    path('user_manage/delete/<int:user_id>/', views.delete_user, name='user_delete'),
    # product delete
    path('product_manage/delete/<int:product_id>/', views.delete_product, name='product_delete'),
    # add_cart
      path('add-to-cart/<int:product_id>/', views.add_cart, name='add_to_cart'),
    path('remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
]
