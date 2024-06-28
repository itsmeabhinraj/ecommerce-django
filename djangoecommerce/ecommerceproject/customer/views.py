from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, get_object_or_404
# Create your views here.
from .models import Cart, CartItem, Order, OrderItem
from shop .models import Product


# Create your views here.


def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart



def add_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(cart_id=_cart_id(request))
        cart.save()
    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        if cart_item.quantity < cart_item.product.stock:
            cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(product=product, quantity=1, cart=cart)
        cart_item.save()
    return redirect('customer:cart_detail')


def cart_detail(request, total=0, counter=0, cart_items=0):
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, active=True)
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            counter += cart_item.quantity
    except ObjectDoesNotExist:
        pass
    return render(request, 'cart.html', dict(cart_items=cart_items, total=total, counter=counter))

def cart_remove(request, product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('customer:cart_detail')


def full_remove(request, product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    cart_item.delete()
    return redirect('customer:cart_detail')

# login page

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                # print("user takend")
                messages.error(request, "Username taken")
                return redirect('customer:signup')
            elif User.objects.filter(email=email).exists():
                # print("email taken")
                messages.info(request, "email taken")
                return redirect('customer:signup')
            else:
                user = User.objects.create_user(username=username, password=cpassword, email=email,
                                                first_name=first_name,
                                                last_name=last_name)
                user.save();
                messages.success(request,
                                 f"Welcome, {username}! Your account has been created successfully. Welcome to Fashion world")
                return redirect('customer:login')
        else:
            # print("password not match")
            messages.info(request, "password is not match")

    return render(request, "signup.html")


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('shop:product_list')
        else:
            messages.error(request, 'invalid credentials.Try again')
            return redirect('customer:login')
    return render(request, 'login.html')


@login_required
def logout(request):
    auth.logout(request)
    messages.success(request, "You have been logged out.")  # Optional: Display a logout message
    # return redirect('customer:login')
    return render(request, 'login.html')

def adminlogin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            if user.is_superuser:
                # Redirect to admin dashboard
                return redirect('customer:admin_loginpage')
            else:
                # Redirect to customer dashboard
                return redirect('shop:product_list')
        else:
            messages.error(request, 'Invalid credentials. Try again.')
            return redirect('customer:login')
    return render(request, 'login.html')

@login_required
def checkout(request):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    cart_items = CartItem.objects.filter(cart=cart, active=True)

    if not cart_items:
        messages.error(request, "Your cart is empty.")
        return redirect('customer:cart_detail')

    order = Order.objects.create(user=request.user, total=0)
    total = 0

    for cart_item in cart_items:
        OrderItem.objects.create(
            order=order,
            product=cart_item.product,
            quantity=cart_item.quantity,
            price=cart_item.product.price
        )
        total += cart_item.product.price * cart_item.quantity
        cart_item.delete()

    order.total = total
    order.save()

    messages.success(request, "Order processed and will be delivered in 5 days.")
    return render(request, 'customer/checkout_success.html')

def checkout_confirmation(request):
    return render(request, 'checkout_confirmation.html')

@login_required
def order_list(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'order_list.html', {'orders': orders})