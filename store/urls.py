from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('deals/', views.deals, name='deals'),
    path('premium-products/', views.premium_products, name='premium_products'),
    path('bestsellers/', views.bestsellers, name='bestsellers'),
    path('pricing/', views.pricing, name='pricing'),
    path('accounts/', views.accounts, name='accounts'),
    path('', views.home, name='home'),
    path('products/', views.product_list, name='product_list'),
    path('add/', views.add_product, name='add_product'),
    path('hygiene/', views.hygiene_info, name='hygiene_info'),
    path('accounts/login/', views.login_view, name='login'),
    path('accounts/logout/', views.logout_view, name='logout'),
    path('accounts/register/', views.register_view, name='register'),
    path('accounts/dashboard/', views.dashboard_view, name='dashboard'),
    path('accounts/profile/', views.profile_view, name='profile'),
    path('smart-recipes/', views.smart_recipes, name='smart_recipes'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='view_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('my-orders/', views.view_orders, name='view_orders'),
    path('place-order/', views.place_order, name='place_order'),
    path('orders/', views.order_history, name='order_history'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/', views.profile, name='profile'),

]