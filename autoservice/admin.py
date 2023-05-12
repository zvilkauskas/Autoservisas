from django.contrib import admin
from .models import CarModel, Car, Service, ServicePrice, Order, OrderList, OrderListReview


class OrderInline(admin.TabularInline):
    model = Order
    # Turn off extra empty lines for input
    extra = 0


class OrderListAdmin(admin.ModelAdmin):
    list_display = ('car', 'order_date', 'user_order', 'order_status')
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
admin.site.register(Order)
admin.site.register(OrderListReview, OrderListReviewAdmin)

