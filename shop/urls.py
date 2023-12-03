from django.urls import path
from . import views


app_name = 'shop'

urlpatterns = [
    path('', views.index_page, name='index'),
    path('shop/shop_menu', views.prod_list, name='shop_menu'),
    path('contact', views.contact_page, name='contact'),
    path('<uuid:category_id>/', views.prod_list, name='products_by_category'),
    path('<uuid:category_id>/<uuid:product_id>/', views.product_detail, name= 'product_detail'),
]
