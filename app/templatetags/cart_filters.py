# Import các module cần thiết
from django import template

# Đăng ký một thư viện template mới
register = template.Library()

# Định nghĩa filter mới
@register.filter
def get_product_quantity(cart, product_id):
    # Chuyển product_id sang chuỗi nếu cần thiết vì keys trong session thường là chuỗi
    product_id_str = str(product_id)
    # Trả về giá trị tương ứng của product_id trong cart, nếu không có trả về 0
    return cart.get(product_id_str, 0)
