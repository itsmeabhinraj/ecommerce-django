from django.urls import path

from . import views
app_name = 'shop'

urlpatterns = [
    path('product_list', views.product_list, name='product_list'),

    path('product_list/', views.product_list, name='product_list'),
    path('product/<int:product_id>/', views.product_detailed, name='product_detailed'),
    path('add_product/', views.add_product, name='add_product'),
    path('all_product/', views.all_product, name='all_product'),
    path('edit_product/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete_product/<int:product_id>/', views.delete_product, name='delete_product'),
    path('', views.demo, name='demo'),
    path('adminpage', views.adminpage, name='adminpage'),
    path('view_users/', views.viewuser, name='viewuser'),
    path('delete_user/', views.delete_user, name='deleteuser'),
    path('checkout/', views.checkout, name='checkout'),

]