import paystackapi.transaction
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.views.generic import *
from django.http import HttpResponse
import urllib.parse
import requests
from django.conf import settings
from django.contrib import messages
from django.urls import reverse
import paystackapi
import random, string
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
    if request.user.is_authenticated:
        products = product.objects.get(pk=product_id)
        if request.method == "POST":
            selected_size = request.POST.get("size")
            existing_cart_item = Cart.objects.filter(user=request.user,product=products, size=selected_size).first()
            if existing_cart_item:
                existing_cart_item.quantity += 1
                existing_cart_item.save()
            else:
                new_cart_item = Cart(user=request.user,product=products, size=selected_size, quantity=1)
                new_cart_item.save()
        return redirect('details',product_id)
    else:
        request.session['add_to_cart_product_id'] = product_id
        request.session['add_to_cart_size'] = request.POST.get("size")
        messages.info(request, 'Please log in to add the item to your cart.')
        return redirect('login')

def cart(request):
    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user)
        return render(request, 'store/cart.html',{'carts':carts})
    else:
        return redirect('login')

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

# def checkout(request):
#     cart_items = Cart.objects.filter(user=request.user)
#     total_price = sum(float(item.product.price.replace(',', '')) * item.quantity for item in cart_items)
#     if request.method == 'POST':
#         order = Order()
#         order.name = request.POST['name']
#         order.address = request.POST['address']
#         order.email = request.POST['email']
#         order.save()
#         for cart_item in cart_items:
#             order_item = Item(stuff=order, product=cart_item.product, quantity=cart_item.quantity,
#                                    size=cart_item.size)
#             order_item.save()
#             cart_item.delete()
#
#         return redirect('home')
#     else:
#         return render(request, 'store/checkout.html', {'cart_items': cart_items, 'total_price':total_price,})


def checkout(request):
    cart_items = Cart.objects.filter(user=request.user)
    total_price = sum(
        float(item.product.price.replace(',', '')) * item.quantity for item in cart_items
    )

    if request.method == 'POST':
        order = Order()
        order.name = request.POST['name']
        order.address = request.POST['address']
        order.email = request.POST['email']
        order.save()
        for cart_item in cart_items:
            order_item = Item(
                stuff=order,
                product=cart_item.product,
                quantity=cart_item.quantity,
                size=cart_item.size,
            )
            order_item.save()
            ref = ''.join(random.choice(string.ascii_lowercase) for i in range(7))
        payment_data = {
            "reference": f"{ref}_{order.id}",
            "amount": int(total_price * 100),
            "currency": "NGN",
            "email": order.email,
            "metadata": {"order_id": order.id},
            "callback_url": request.build_absolute_uri(reverse('payment_callback')),
        }
        # encoded_data = urllib.parse.urlencode(payment_data)
        # paystack_payment_url = f"https://checkout.paystack.com/?{encoded_data}"
        # return redirect(paystack_payment_url)
        transaction = paystackapi.transaction.Transaction.initialize(**payment_data)
        return redirect(transaction['data']['authorization_url'])

    else:
        return render(
            request,
            'store/checkout.html',
            {'cart_items': cart_items, 'total_price': total_price},
        )

def payment_callback(request):
    reference = request.GET.get('reference')
    verify_transaction = paystackapi.transaction.Transaction.verify(reference)

    # Check if the payment is successful
    if verify_transaction['data']['status'] == 'success':
        # Update your order status or perform other actions
        order_id = int(request.GET['order_id'])
        order = Order.objects.get(id=order_id)
        order.paid = True
        order.save()

        return HttpResponse("Payment successful")
    else:
        return HttpResponse("Payment failed")
    # response = requests.get(
    #     f"https://api.paystack.co/transaction/verify/{reference}",
    #     headers={"Authorization": f"Bearer {settings.PAYSTACK_SECRET_KEY}"},
    # )
    # if response.status_code == 200:
    #     payment_data = response.json()
    #     if payment_data['data']['status'] == 'success':
    #         # Update the order status to "Paid" or perform other necessary actions
    #         order_id = payment_data['data']['metadata']['order_id']
    #         order = Order.objects.get(pk=order_id)
    #         order.payment_status = True
    #         order.save()
    #         Cart.objects.filter(user=request.user).delete()
    #         return render(request, 'store/success.html', {'order': order})
    # return render(request, 'store/error.html', {'error_message': 'Payment failed'})

def search(request):
   s_query = request.GET.get('search')
   products = []
   if s_query:
       products = product.objects.filter(name__icontains=s_query)

   return render(request, 'store/search.html', {'s_query': s_query, 'products': products})
