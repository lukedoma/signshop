from django.urls import path
from .views import (
    ItemDetailView,
    CheckoutView,
    HomeView,
    OrderSummaryView,
    add_to_cart,
    remove_from_cart,
    remove_single_item_from_cart,
    PaymentView,
    AddCouponView
    # RequestRefundView
)

app_name = 'core'

urlpatterns = [
    # path('', item_list, name='item-list')
    path('', HomeView.as_view(), name='home'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),
    path('order-summary/', OrderSummaryView.as_view(), name="order-summary"),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('add-to-cart/<slug>', add_to_cart, name='add-to-cart'),
    path('remove_from_cart/<slug>', remove_from_cart, name='remove_from_cart'),
    path('remove-single-item-from-cart/<slug>',
         remove_single_item_from_cart, name='remove-single-item-from-cart'),
    path('payment/<payment_option>', PaymentView.as_view(), name='payment')

]
