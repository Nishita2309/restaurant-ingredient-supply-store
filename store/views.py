from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm

def home(request):
    return render(request, 'store/home.html')


def product_list(request):
    products = Product.objects.all()
    return render(request, 'store/product_list.html', {'products': products})

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'store/add_product.html', {'form': form})

def index(request):
    print(">>> Index View Loaded <<<")
    return render(request, 'store/index.html')

def deals(request):
    products = Product.objects.filter(on_deal=True).order_by('-available')
    return render(request, 'store/deals.html', {'products': products})

def bestsellers(request):
    products = Product.objects.filter(is_bestseller=True).order_by('-available')
    return render(request, 'store/bestsellers.html', {'products': products})


def premium_products(request):
    products = Product.objects.filter(is_premium=True).order_by('-available')
    return render(request, 'store/premium_products.html', {'products': products})

def pricing(request):
    return render(request, 'store/pricing.html')

def accounts(request):
    return render(request, 'store/accounts.html')

def hygiene_info(request):
    return render(request, 'store/hygiene_info.html')


from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username, email, password)
        messages.success(request, "Account created successfully!")
        return redirect('login')
    return render(request, 'store/register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid credentials")
    return render(request, 'store/login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard_view(request):
    return render(request, 'store/dashboard.html')

@login_required
def profile_view(request):
    return render(request, 'store/profile.html')

def smart_recipes(request):
    return render(request, 'store/smart_recipes.html')

from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Product, Cart

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = Cart.objects.get_or_create(user=request.user, product=product)

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('view_cart')  # we'll create this view next


from django.contrib.auth.decorators import login_required
from django.db.models import F, Sum

@login_required
def view_cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    total_price = cart_items.aggregate(
        total=Sum(F('product__price') * F('quantity'))
    )['total'] or 0

    return render(request, 'store/cart.html', {
        'cart_items': cart_items,
        'total_price': total_price,
    })

from .models import Order, OrderItem

@login_required
def checkout(request):
    cart_items = Cart.objects.filter(user=request.user)
    if not cart_items:
        return redirect('view_cart')

    total = sum(item.product.price * item.quantity for item in cart_items)
    order = Order.objects.create(user=request.user, total_amount=total)

    for item in cart_items:
        OrderItem.objects.create(
            order=order,
            product=item.product,
            quantity=item.quantity
        )
    cart_items.delete()

    return render(request, 'store/checkout_success.html', {'order': order})

from .models import Order

@login_required
def view_orders(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'store/my_orders.html', {'orders': orders})

@login_required
def place_order(request):
    cart = request.session.get('cart', {})
    if not cart:
        return redirect('view_cart')

    order = Order.objects.create(user=request.user, total_amount=0)
    total = 0

    for product_id, quantity in cart.items():
        product = Product.objects.get(id=product_id)
        OrderItem.objects.create(order=order, product=product, quantity=quantity)
        total += product.price * quantity

    order.total_amount = total
    order.save()

    # Clear the cart
    request.session['cart'] = {}

    return redirect('order_history')


from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Order

@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')

    # Calculate subtotal for each item
    for order in orders:
        for item in order.items.all():
            item.subtotal = item.product.price * item.quantity

    return render(request, 'store/order_history.html', {'orders': orders})

from django.shortcuts import render

def dashboard(request):
    return render(request, 'store/dashboard.html')

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    return render(request, 'store/profile.html')

@login_required
def profile(request):
    is_embed = request.GET.get('embed') == 'true'
    template = 'store/profile_embed.html' if is_embed else 'store/profile.html'
    return render(request, template)

def profile(request):
    embed = request.GET.get('embed') == 'true'
    return render(request, 'store/profile.html', {'embed': embed})

def accounts_view(request):
    return render(request, 'accounts.html')

def login_view(request):
    template = 'store/login.html' if request.GET.get('embed') != 'true' else 'store/login_embed.html'
    return render(request, template)


def login_view(request):
    if request.GET.get('embed') == 'true':
        return render(request, 'store/login.html')  # or login_embed.html if you created it
    else:
        return render(request, 'store/login.html')  # regular page load

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # or wherever you want to redirect
        else:
            messages.error(request, 'Invalid username or password')

    # Handle embed mode
    if request.GET.get('embed') == 'true':
        return render(request, 'store/login.html')  # or 'store/login_embed.html' if you have a separate one
    return render(request, 'store/login.html')
