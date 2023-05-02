from django.contrib import admin
from .models import CarModel, Car, Service, ServicePrice, Order, OrderList


class OrderInline(admin.TabularInline):
    model = Order
    # Turn off extra empty lines for input
    extra = 0


class OrderListAdmin(admin.ModelAdmin):
    list_display = ('car', 'order_date')
    inlines = [OrderInline]


class CarAdmin(admin.ModelAdmin):
    list_display = ('client', 'car_model', 'plate_number', 'vin_number')
    list_filter = ('client', 'car_model')
    search_fields = ('client', 'plate_number', 'vin_number')

class ServicePriceAdmin(admin.ModelAdmin):
    list_display = ('service', 'price')


admin.site.register(CarModel)
admin.site.register(Car, CarAdmin)
admin.site.register(Service)
admin.site.register(ServicePrice, ServicePriceAdmin)
admin.site.register(OrderList, OrderListAdmin)
admin.site.register(Order)

