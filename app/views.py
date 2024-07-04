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
def home_admin(request):
    return render(request, 'admin/base.html')
