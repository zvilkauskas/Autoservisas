from django.contrib import admin
from .models import CarModel, Car, Service, ServicePrice, Order, OrderList, OrderListReview


class OrderInline(admin.TabularInline):
    model = Order
    # Turn off extra empty lines for input
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'service', 'quantity', 'price', 'total_order_price',)

    def total_order_price(self, obj):
        return obj.total_order_price


class OrderListAdmin(admin.ModelAdmin):
    list_display = ('car', 'order_date', 'user_order', 'order_status', 'total_order_list_price')
    inlines = [OrderInline]
    fieldsets = (
        (None, {'fields': ('car',)}),
        ('Service status', {'fields': ('order_status', 'user_order', 'due_back')}),
    )


class CarAdmin(admin.ModelAdmin):
    list_display = ('client', 'car_model', 'plate_number', 'vin_number')
    list_filter = ('client', 'car_model')
    search_fields = ('client', 'plate_number', 'vin_number')


class ServicePriceAdmin(admin.ModelAdmin):
    list_display = ('service', 'price')

class OrderListReviewAdmin(admin.ModelAdmin):
    list_display = ('order_list', 'date_created', 'reviewer', 'content')


admin.site.register(CarModel)
admin.site.register(Car, CarAdmin)
admin.site.register(Service)
admin.site.register(ServicePrice, ServicePriceAdmin)
admin.site.register(OrderList, OrderListAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderListReview, OrderListReviewAdmin)

