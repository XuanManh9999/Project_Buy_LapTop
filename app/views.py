from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'common/products.html')
def checkout(request):
    return render(request, 'common/checkout.html')
def detail_product(request):
    return render(request, 'common/detail_product.html')
def store(request):
    return render(request, 'common/store.html')
def login(request):
    return render(request, 'common/login.html')
def register(request):
    return render(request, 'common/register.html')
def forgot_password(request):
    return render(request, 'common/forgot_password.html')
# admin
def home_manage(request):
    return render(request, 'manage/base.html')
def product_manage(request):
    return render(request, 'manage/manage_product.html')
def order_manage(request):
    return render(request, 'manage/manage_order.html')
def user_manage(request):
    return render(request, 'manage/manage_user.html')
