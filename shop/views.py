from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.shortcuts import render, get_object_or_404

from .models import Category, Product


def index_page(request):
    return render(request, 'index.html', {})


def contact_page(request):
    return render(request, 'contact.html', {})


def pizzas_category(request):
    pizza_products = Product.objects.filter(category__name='Chicken')
    return render(request, 'shop/pizzas_category.html', {'pizza_products': pizza_products})


def chicken_category(request):
    chicken_products = Product.objects.filter(category__name='Chicken')
    return render(request, 'shop/chicken_category.html', {'chicken_products': chicken_products})


def sides_category(request):
    sides_products = Product.objects.filter(category__name='Sides')
    return render(request, 'shop/sides_category.html', {'sides_products': sides_products})


def drinks_category(request):
    drinks = Product.objects.filter(category__name='Drinks')
    paginator = Paginator(drinks, 12)  # Adjust the number of items per page as needed

    page = request.GET.get('page')
    try:
        drinks = paginator.page(page)
    except PageNotAnInteger:
        drinks = paginator.page(1)
    except EmptyPage:
        drinks = paginator.page(paginator.num_pages)

    return render(request, 'shop/drinks_category.html', {'drinks': drinks})


def prod_list(request, category_id=None):
    category = None
    products = Product.objects.filter(available=True)

    # Check if the category_id is provided
    if category_id:
        # If the category_id is "pizzas", set the category to the Pizza category
        if category_id == "pizzas":
            category = get_object_or_404(Category, name="Pizzas")
        else:
            category = get_object_or_404(Category, id=category_id)

        # Filter products based on the selected category
        products = Product.objects.filter(category=category, available=True)

    paginator = Paginator(products, 6)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        products = paginator.page(page)
    except (EmptyPage, InvalidPage):
        products = paginator.page(paginator.num_pages)

    return render(request, 'shop/category.html', {'category': category, 'prods': products})


def product_detail(request, category_id, product_id):
    product = get_object_or_404(Product, category_id=category_id, id=product_id)
    return render(request, 'shop/product.html', {'product': product})
