from django.shortcuts import render
from .models import CarModel, Car, Service, ServicePrice, OrderList, Order
from django.views import generic
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q

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
# def registered_car_models(request):
#     registered_cars = Car.objects.all()
#     context = {
#         'registered_cars_models': registered_cars
#     }
#     return render(request, 'registered_car_models.html', context)

#paginatoriaus perdarymas
class CarListView(generic.ListView):
    model = Car
    paginate_by = 2
    template_name = 'registered_car_models.html'


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
    paginator = Paginator(OrderList.objects.all(), 2)
    page_number = request.GET.get('page')
    paged_orders = paginator.get_page(page_number)
    if page_number is None:
        page_num = 1
    else:
        page_num = page_number
    return render(request, 'orders.html', {'orders': paged_orders, 'page_obj': paginator.page(page_num)})

def specific_order(request, order_list_id):
    order_list = get_object_or_404(OrderList, pk=order_list_id)
    orders_of_order_list = Order.objects.filter(order_list_id__exact=order_list_id)
    context = {
        'order_list': order_list,
        'orders': orders_of_order_list
    }
    return render(request, 'specific_order.html', context)

def search_car(request):
    query = request.GET.get('query')
    search_results = Car.objects.filter(Q(client__icontains=query)
                                        | Q(car_model__car_model__icontains=query)
                                        | Q(car_model__brand__icontains=query)
                                        | Q(plate_number__icontains=query)
                                        | Q(vin_number__icontains=query))
    return render(request, 'search_cars.html', {'cars': search_results, 'query': query})


