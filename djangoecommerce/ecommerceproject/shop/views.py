from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect

from .forms import ProductForm
from .models import Product


# Create your views here.
def product_list(request):
    products = Product.objects.all()
    # categories = Category.objects.all()

    return render(request, 'product_list.html', {'products': products})  # ,'categories': categories


def product_detailed(request, product_id):
    product = get_object_or_404(Product, pk=product_id)  # Fetching the first book
    return render(request, 'product_detailed.html', {'product': product})


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, )
        if form.is_valid():
            movie = form.save(commit=False)
            movie.save()
            return redirect('shop:product_list')
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})


def all_product(request):
    # Retrieve movies added by the current logged-in user
    products = Product.objects.all()
    return render(request, 'allproductlist.html', {'products': products})


def edit_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('shop:product_list')
    else:
        form = ProductForm(instance=product)

    return render(request, 'edit_product.html', {'form': form})


def delete_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        product.delete()
        return redirect('shop:all_product')

    return render(request, 'delete_product.html', {'product': product})


def demo(request):
    return render(request, "index.html")


def adminpage(request):
    return render(request, "adminpage.html")
def checkout(request):
    return render(request, "checkout.html")



def viewuser(request):
    if not request.user.is_superuser:
        return redirect('home')  # Redirect if user is not an admin

    users = User.objects.all()
    return render(request, 'view_users.html', {'users': users})


def delete_user(request, user_id):
    if not request.user.is_superuser:
        return redirect('shop:product_list')  # Redirect if user is not an admin

    user = get_object_or_404(User, pk=user_id)
    if request.method == 'POST':
        user.delete()
        return redirect('shop:viewuser')  # Redirect after deletion

    # Handle GET request (display confirmation page)
    return render(request, 'delete_user.html', {'user': user})
