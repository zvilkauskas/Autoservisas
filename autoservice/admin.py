from django.contrib import admin
from .models import CarModel, Car, Service, ServicePrice, Order

class CarAdmin(admin.ModelAdmin):
    list_display = ('client', 'car_model', 'plate_number', 'vin_number')
    list_filter = ('client', 'car_model')
    search_fields = ('client', 'plate_number', 'vin_number')


admin.site.register(CarModel)
admin.site.register(Car, CarAdmin)
admin.site.register(Service)
admin.site.register(ServicePrice)
admin.site.register(Order)

# FIXME: Is this logical?
#admin.site.register(OrderInstance)
