from django.urls import path
from . import views


app_name = 'shop'

urlpatterns = [
    path('', views.prod_list, name='all_products'),
    path('<uuid:category_id>/', views.prod_list, name='products_by_category'),
    path('<uuid:category_id>/<uuid:product_id>/', views.product_detail, name= 'product_detail'),
    path('pizzas/', views.pizzas_category, name='pizzas_category'),  # Add this line
    path('categories/chicken/', views.chicken_category, name='chicken_category'),
    path('categories/drinks/', views.drinks_category, name='drinks_category'),
    path('categories/sides/', views.sides_category, name='sides_category'),

   
    
    
]
