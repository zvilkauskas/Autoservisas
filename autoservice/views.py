from django.shortcuts import render
from .models import CarModel, Car, Service, ServicePrice, OrderList, Order
from django.views import generic

def index(request):
    registered_cars_models_count = CarModel.objects.all().count()
    services = Service.objects.all()
    services_count = Service.objects.all().count()
    context = {
        'registered_cars_models_count': registered_cars_models_count,
        'services': services,
        'services_count': services_count,
    }
    return render(request, 'index.html', context)
def registered_car_models(request):
    registered_cars = Car.objects.all()
    context = {
        'registered_cars_models': registered_cars
    }
    return render(request, 'registered_car_models.html', context)

def specific_car(request, car_id):
    car = Car.objects.get(car_id=car_id)
    context = {
        'car_info': car
    }
    return render(request, 'specific_car.html', context)

def services(request):
    all_services = Service.objects.all()
    context = {
        'services': all_services
    }
    return render(request, 'services.html', context)

def orders(request):
    all_orders = OrderList.objects.all()
    context = {
        'orders': all_orders
    }
    return render(request, 'orders.html', context)
def specific_order(request, order_id):
    pass