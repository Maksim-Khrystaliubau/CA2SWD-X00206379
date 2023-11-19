from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from django.core.paginator import Paginator, EmptyPage, InvalidPage



def pizzas_category(request):
    # Add logic to retrieve and display pizza products
    return render(request, 'shop/pizzas_category.html', {})


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
        products = paginator.page(paginator.num_pages())

    return render(request, 'shop/category.html', {'category': category, 'prods': products})

def product_detail(request, category_id, product_id):
    product = get_object_or_404(Product, category_id=category_id, id=product_id)
    return render(request, 'shop/product.html', {'product': product})
