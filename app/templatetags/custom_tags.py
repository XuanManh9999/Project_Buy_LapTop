from django import template

register = template.Library()

@register.filter
def get_product_quantity(cart, product_id):
    return cart.get(str(product_id), 0)
