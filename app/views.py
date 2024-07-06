from django.shortcuts import render, redirect
from .models import NguoiDung
from django.contrib import messages
# import add_message

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
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = NguoiDung.objects.filter(email=email, mat_khau=password)
        if user:
            # luu thong toan bo thong tin nguoi dung vao section
            request.session['id'] = user[0].id
            request.session['user'] = user[0].ho_va_ten
            request.session['email'] = user[0].email
            request.session['vai_tro'] = user[0].vai_tro
            # check vai_tro
            if user[0].vai_tro == "admin":
                return render(request, 'manage/base.html')
            else:
                return render(request, 'common/products.html')
        else:
            messages.warning(request, 'Email hoặc mật khẩu không đúng')
            return render(request, 'common/login.html')
    
    return render(request, 'common/login.html')
def register(request):
    if request.method == 'POST':
        ho_va_ten = request.POST.get('name')
        email = request.POST.get('email')
        mat_khau = request.POST.get('password')
        vai_tro = 'user'
        NguoiDung.objects.create(ho_va_ten=ho_va_ten, email=email, mat_khau=mat_khau, vai_tro=vai_tro)
        messages.success(request, 'Đăng ký tài khoản thành công')
        return render(request, 'common/login.html')
    return render(request, 'common/register.html')
def forgot_password(request):
    if request.method == 'POST':
        # kiem tra xem email co hop le khong, neu hop le thi gui mat khau moi ve
        email = request.POST.get('email')
        user = NguoiDung.objects.filter(email=email)
        if user:
            messages.success(request, 'Mật khẩu của bạn là: ' + user[0].mat_khau)
            return render(request, 'common/login.html')
        else:
            messages.error(request, 'Email không tồn tại')
            return render(request, 'common/forgot_password.html')
    return render(request, 'common/forgot_password.html')
# admin
def home_manage(request):
     # Kiểm tra nếu người dùng không phải admin, chuyển hướng đến trang đăng nhập
    if request.session.get('vai_tro') != 'admin':
        return redirect('login')
    return render(request, 'manage/base.html')
def product_manage(request):
        # Kiểm tra nếu người dùng không phải admin, chuyển hướng đến trang đăng nhập
    if request.session.get('vai_tro') != 'admin':
        return redirect('login')
    return render(request, 'manage/manage_product.html')
def order_manage(request):
    # Kiểm tra nếu người dùng không phải admin, chuyển hướng đến trang đăng nhập
    if request.session.get('vai_tro') != 'admin':
        return redirect('login')
    return render(request, 'manage/manage_order.html')
def user_manage(request):
     # Kiểm tra nếu người dùng không phải admin, chuyển hướng đến trang đăng nhập
    if request.session.get('vai_tro') != 'admin':
        return redirect('login')
    return render(request, 'manage/manage_user.html')
def logout_view(request):
    # Xóa session để đăng xuất người dùng
    request.session.flush()
    return redirect('login')
