from django.contrib import admin

from .models import Item,Articles,Contact, OrderItem, Order, Payment, Coupon, Refund, Address


def make_refund_accepted(modeladmin, request, queryset):
    queryset.update(refund_requested=False, refund_granted=True)


make_refund_accepted.short_description = 'Update orders to refund granted'


class OrderAdmin(admin.ModelAdmin):
    list_display = ['user',
                    'ordered',
                    'being_delivered',
                    'received',
                    'refund_requested',
                    'refund_granted',
                    'shipping_address',
                    'billing_address',
                    'payment',
                    'coupon'
                    ]
    list_display_links = [
        'user',
        'shipping_address',
        'billing_address',
        'payment',
        'coupon'
    ]
    list_filter = ['ordered',
                   'being_delivered',
                   'received',
                   'refund_requested',
                   'refund_granted']
    search_fields = [
        'user__username',
        'ref_code'
    ]
    actions = [make_refund_accepted]


class AddressAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'street_address',
        'apartment_address',
        'country',
        'zip',
        'address_type',
        'default'
    ]
    list_filter = ['default', 'address_type', 'country']
    search_fields = ['user', 'street_address', 'apartment_address', 'zip']

class ItemAdmin(admin.ModelAdmin):
    list_display = ['title',
                    'price',
                    'discount_price',
                    'category'
                   
                    ]
    list_display_links = [
        'title'
        
    ]
    list_filter = ['category'
                   ]
    search_fields = [
        'title',
        
    ]
    prepopulated_fields = {"slug": ("title",)}
class ArticlesAdmin(admin.ModelAdmin):
    list_display = ['article_title',
                   
                    'article_category'
                   
                    ]
    list_display_links = [
        'article_title'
        
    ]
    list_filter = ['article_category'
                   ]
    search_fields = [
        'article_title',
        
    ]   
    prepopulated_fields = {"article_slug": ("article_title",)} 
class CouponAdmin(admin.ModelAdmin):
    list_display = ['code',
                    'amount'
                   
                    ]
    list_display_links = [
        'code'
        
    ]
    
    search_fields = [
        'code',
        
    ]
    




admin.site.register(Item,ItemAdmin)
admin.site.register(Articles,ArticlesAdmin)
admin.site.register(OrderItem)
admin.site.register(Contact)
admin.site.register(Order, OrderAdmin)
admin.site.register(Payment)
admin.site.register(Coupon,CouponAdmin)
admin.site.register(Refund)
admin.site.register(Address, AddressAdmin)
# admin.site.register(UserProfile)
