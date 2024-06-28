from django.urls import path
from . import views

app_name = 'customer'
urlpatterns = [
    path('add/<int:product_id>/', views.add_cart, name="add_cart"),
    path('details/', views.cart_detail, name='cart_detail'),
    path('remove/<int:product_id>/',views.cart_remove,name="cart_remove"),
    path('full_remove/<int:product_id>/', views.full_remove, name="full_remove"),

    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('admin/loginpage',views.adminlogin,name='adminlogin'),
    path('orders/', views.order_list, name='order_list'),  # New URL pattern for order list
    path('checkout/', views.checkout, name='checkout'),  # New URL pattern for checkout
]
