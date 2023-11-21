from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from .models import Order, OrderItem

def thanks(request, order_id):
    if order_id:
        customer_order = get_object_or_404(Order, id=order_id)
        return render(request, 'thanks.html', {'customer_order': customer_order})
    return render(request, 'thanks.html')  # Handle the case where order_id is not provided

class OrderHistory(LoginRequiredMixin, View):
    def get(self, request):
        if request.user.is_authenticated:
            email = str(request.user.email)
            order_details = Order.objects.filter(emailAddress=email)

            # Iterate through the orders and calculate the total for each
            for order in order_details:
                order.calculate_total()

            return render(request, 'order/orders_list.html', {'order_details': order_details})
        return render(request, 'order/orders_list.html')  # Handle the case where the user is not authenticated

class OrderDetail(LoginRequiredMixin, View):
    def get(self, request, order_id):
        if request.user.is_authenticated:
            email = str(request.user.email)
            order = get_object_or_404(Order, id=order_id, emailAddress=email)
            order_items = OrderItem.objects.filter(order=order)

            return render(request, 'order/order_detail.html', {'order': order, 'order_items': order_items})
        return render(request, 'order/order_detail.html')  # Handle the case where the user is not authenticated
