from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.views.generic import *
from django.urls import reverse_lazy
# Create your views here.
class home(ListView):
    model = product
    template_name = 'store/index.html'

def shirts_view(request):
    shirts_category = Category.objects.get(cat_name='Shirts')
    products = product.objects.filter(category=shirts_category)
    return render(request, 'store/shirts.html', {'products': products})

def sweats_view(request):
    shirts_category = Category.objects.get(cat_name='Sweats/hoodies')
    products = product.objects.filter(category=shirts_category)
    return render(request, 'store/hoodie.html', {'products': products})
def shorts_view(request):
    shirts_category = Category.objects.get(cat_name='Shorts/Cargos')
    products = product.objects.filter(category=shirts_category)
    return render(request, 'store/shorts.html', {'products': products})
def accessories_view(request):
    shirts_category = Category.objects.get(cat_name='Accessories')
    products = product.objects.filter(category=shirts_category)
    return render(request, 'store/accessories.html', {'products': products})

def product_detail(request, product_id):
    products = product.objects.get(pk=product_id)
    return render(request, 'store/details.html', {'products': products})

def add_to_cart(request, product_id):
    products = product.objects.get(pk=product_id)
    if request.method == "POST":
        selected_size = request.POST.get("size")

        # Check if a cart item with the same product and size already exists
        existing_cart_item = Cart.objects.filter(product=products, size=selected_size).first()

        if existing_cart_item:
            # If the same product and size combination already exists in the cart, increase quantity
            existing_cart_item.quantity += 1
            existing_cart_item.save()
        else:
            # If it's a new product and size combination, create a new cart item
            new_cart_item = Cart(product=products, size=selected_size, quantity=1)
            new_cart_item.save()

        # Cart.size = request.POST.get("size")
        # cart_item, created = Cart.objects.get_or_create(product=products)
        # if not created:
        #     cart_item.quantity += 1
        #     cart_item.save()
    return redirect('details',product_id)

def cart(request):
    carts = Cart.objects.all()
    return render(request, 'store/cart.html',{'carts':carts})

def cart_remove(request, cart_item_id):
    kart = get_object_or_404(Cart, pk=cart_item_id)
    kart.delete()
    return redirect('cart_item')
def cart_update(request, cart_item_id):
    kart = get_object_or_404(Cart, pk=cart_item_id)
    if request.method == 'POST':
        new_quantity = int(request.POST.get('quantity'))
        kart.quantity = new_quantity
        kart.save()
    return redirect('cart_item')

def checkout(request):
    if request.method == 'POST':
        order = Order()
        order.name = request.POST['name']
        order.address = request.POST['address']
        order.save()
        Cart.objects.filter().delete()
        return redirect('home')
    else:
        cart_items = Cart.objects.all()
        total_price = sum(float(item.product.price.replace(',',''))*item.quantity for item in cart_items)
        return render(request, 'store/checkout.html', {'cart_items': cart_items, 'total_price':total_price})

