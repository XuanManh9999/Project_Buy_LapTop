from django.shortcuts import render, redirect, get_object_or_404
from .models import NguoiDung, SanPham
from django.contrib import messages
import locale
# import add_message

# Create your views here.
def index(request):
     # Lấy giỏ hàng từ session
    cart = request.session.get('cart', {})
    
    # Lấy danh sách các sản phẩm từ giỏ hàng
    product_ids = cart.keys()
    products_in_cart = SanPham.objects.filter(id__in=product_ids)
    # Tính toán tổng số lượng và tổng tiền
    total_quantity = sum(cart[str(product.id)] for product in products_in_cart)
    total_price = sum(product.gia_san_pham * cart[str(product.id)] for product in products_in_cart)
    
    # Định dạng tiền tệ cho giá sản phẩm
    locale.setlocale(locale.LC_ALL, 'vi_VN')
    for product in products_in_cart:
        product.gia_san_pham = locale.currency(product.gia_san_pham, grouping=True)
    # lay all product
    products = SanPham.objects.all()
    return render(request, 'common/products.html', {
        'products': products,
        'total_quantity': total_quantity,
        'total_price': locale.currency(total_price, grouping=True),
        'products_in_cart': products_in_cart,
        'cart': cart,
    })
def checkout(request):
    # kiem tra xem nguoi dung da dang nhap chua
    if not request.session.get('id'):
        return redirect('login')
    # Lấy giỏ hàng từ session
    cart = request.session.get('cart', {})

    # Lấy danh sách các sản phẩm từ giỏ hàng
    product_ids = cart.keys()
    products_in_cart = SanPham.objects.filter(id__in=product_ids)

    # Tính toán tổng số lượng và tổng tiền
    total_quantity = sum(cart[str(product.id)] for product in products_in_cart)
    total_price = sum(product.gia_san_pham * cart[str(product.id)] for product in products_in_cart)

    # Định dạng tiền tệ cho giá sản phẩm
    locale.setlocale(locale.LC_ALL, 'vi_VN')
    for product in products_in_cart:
        product.gia_san_pham = locale.currency(product.gia_san_pham, grouping=True)

    # Trả về template với context
    return render(request, 'common/checkout.html', {
        'cart_product': products_in_cart,
        'total_quantity': total_quantity,
        'price_products': locale.currency(total_price, grouping=True),
        'cart': cart,
    })

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
                #chuyen huong ve trang index
                return redirect('index')
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
    if request.session.get('vai_tro') != 'admin':
        return redirect('login')
    if request.method == 'POST':
        # lay du lieu tu form
        product_id = request.POST.get('ID')
        name = request.POST.get('name')
        price = request.POST.get('price')
        description = request.POST.get('desc')
        quantity = request.POST.get('quantity')
        url = request.POST.get('url')
        type_product = request.POST.get('type_product')
        if product_id:
            product = SanPham.objects.get(id=product_id)
            product.ten_san_pham = name
            product.gia_san_pham = price
            product.mo_ta_san_pham = description
            product.so_luong_san_pham = quantity
            product.hinh_anh_san_pham = url
            product.loai_san_pham = type_product
            product.save()
            messages.success(request, 'Cập nhật sản phẩm thành công')
        else:
            product = SanPham()
            product.ten_san_pham = name
            product.gia_san_pham = price
            product.mo_ta_san_pham = description
            product.so_luong_san_pham = quantity
            product.hinh_anh_san_pham = url
            product.loai_san_pham = type_product
            product.save()
            messages.success(request, 'Thêm sản phẩm thành công')
        return redirect('product_manage')
    # Lấy tất cả sản phẩm từ database
    products = SanPham.objects.all()        
    return render(request, 'manage/manage_product.html', {'products': products})
def order_manage(request):
    # Kiểm tra nếu người dùng không phải admin, chuyển hướng đến trang đăng nhập
    if request.session.get('vai_tro') != 'admin':
        return redirect('login')
    return render(request, 'manage/manage_order.html')
def user_manage(request):
    # Kiểm tra nếu người dùng không phải admin, chuyển hướng đến trang đăng nhập
    if request.session.get('vai_tro') != 'admin':
        return redirect('login')

    if request.method == 'POST':
        # Lấy dữ liệu từ form
        user_id = request.POST.get('id')
        name = request.POST.get('name')
        date = request.POST.get('date')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')
        address = request.POST.get('address')
        role = request.POST.get('role')
        if user_id:  # Nếu ID tồn tại, cập nhật người dùng
            user = NguoiDung.objects.get(id=user_id)
            user.ho_va_ten = name
            user.ngay_sinh = date if date else None 
            user.so_dien_thoai = phone
            user.email = email
            user.mat_khau = password
            user.dia_chi = address
            user.vai_tro = role
            user.save()
            messages.success(request, 'Cập nhật người dùng thành công')
        else:  # Nếu không, tạo người dùng mới
            user = NguoiDung()
            user.ho_va_ten = name
            user.ngay_sinh = date
            user.so_dien_thoai = phone
            user.email = email
            user.mat_khau = password
            user.dia_chi = address
            user.vai_tro = role
            user.save()
            messages.success(request, 'Thêm người dùng thành công')
        return redirect('user_manage')

    # Lấy tất cả người dùng từ database
    users = NguoiDung.objects.all()
    return render(request, 'manage/manage_user.html', {'users': users})

def delete_user(request, user_id):
    # Kiểm tra nếu người dùng không phải admin, chuyển hướng đến trang đăng nhập
    if request.session.get('vai_tro') != 'admin':
        return redirect('login')

    user = get_object_or_404(NguoiDung, id=user_id)
    user.delete()
    messages.success(request, 'Người dùng đã được xóa thành công')
    return redirect('user_manage')

def delete_product(request, product_id):
    # Kiểm tra nếu người dùng không phải admin, chuyển hướng đến trang đăng nhập
    if request.session.get('vai_tro') != 'admin':
        return redirect('login')
    product = get_object_or_404(SanPham, id=product_id)
    product.delete()
    messages.success(request, 'Sản phẩm đã được xóa thành công')
    return redirect('product_manage')
        

def logout_view(request):
    # Xóa session để đăng xuất người dùng
    request.session.flush()
    return redirect('login')

def add_cart(request, product_id):
    # Kiểm tra xem người dùng đã đăng nhập chưa
    if not request.session.get('id'):
        return redirect('login')

    # Lấy giỏ hàng từ session
    cart = request.session.get('cart', {})

    # Chuyển đổi product_id sang chuỗi nếu cần thiết
    product_id_str = str(product_id)

    # Kiểm tra xem sản phẩm đã có trong giỏ hàng chưa
    if product_id_str in cart:
        # Nếu có rồi thì tăng số lượng lên 1
        cart[product_id_str] += 1
    else:
        # Nếu chưa có thì thêm sản phẩm vào giỏ hàng với số lượng là 1
        cart[product_id_str] = 1

    # Lưu giỏ hàng vào session
    request.session['cart'] = cart


    return redirect('index')

    
def remove_from_cart(request, product_id):
    # Lấy giỏ hàng từ session
    cart = request.session.get('cart', {})

    # Chuyển đổi product_id sang chuỗi nếu cần thiết
    product_id_str = str(product_id)

    # Kiểm tra xem sản phẩm có trong giỏ hàng không
    if product_id_str in cart:
        # Nếu có, xóa sản phẩm khỏi giỏ hàng
        del cart[product_id_str]

        # Cập nhật lại giỏ hàng trong session
        request.session['cart'] = cart

    # Chuyển hướng về trang index hoặc trang giỏ hàng (tuỳ theo yêu cầu của bạn)
    return redirect('index')  # Thay 'index' bằng tên của URL pattern cho trang hiển thị giỏ hàng    
    