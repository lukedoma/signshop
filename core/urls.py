from django.urls import path,reverse
from django.conf.urls import url
from django.views.generic import RedirectView

from django.views.decorators.csrf import csrf_exempt
from .views import (
    ItemDetailView,
    CheckoutView,
    HomeView,
    OrderSummaryView,
    NewssingleView,
    add_to_cart,
    remove_from_cart,
    remove_single_item_from_cart,
    search,
    AboutusView,
    ContactView,
    NewsView,
    # PaymentView,
    AddCouponView,
    RequestRefundView,
    PaypalView,
    PaypalSuccess,
    paymentComplete
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
    path('search', csrf_exempt(search), name='search'),
    path('remove_from_cart/<slug>', remove_from_cart, name='remove_from_cart'),
    path('remove-single-item-from-cart/<slug>',
         remove_single_item_from_cart, name='remove-single-item-from-cart'),
    path('payment/<payment_option>', PaypalView.as_view(), name='paypal'),
    path('payment/<payment_option2>', PaypalView.as_view(), name='paypal'),
    path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),
    path('about_us/', AboutusView.as_view(), name='about_us'),
    path('contact_us/', ContactView.as_view(), name='contact_us'),
    path('news/', NewsView.as_view(), name='news'),
    path('news_single/', NewssingleView.as_view(), name='news_single'),
    path('request-refund/', RequestRefundView.as_view(), name='request-refund'),
    path('paypal-success/(?P<order_id>\d+)/', csrf_exempt(PaypalSuccess.as_view()), name='paypal-success'),
    path('complete/',paymentComplete, name="complete"),
    # url(r'^paypal-success/$', csrf_exempt(PaypalSuccess.as_view()), name='paypal-success'),
    

]
