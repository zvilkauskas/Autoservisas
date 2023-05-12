from django.shortcuts import render
from .models import CarModel, Car, Service, ServicePrice, OrderList, Order, OrderListReview
from django.views import generic
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.decorators import login_required

# Registracijos importai
from django.shortcuts import redirect
from django.contrib.auth.forms import User
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages

# Reviews importai
from django.shortcuts import render, reverse, get_object_or_404

# Importuojame FormMixin, kurį naudosime BookDetailView klasėje
from django.views.generic.edit import FormMixin

def index(request):
    registered_cars_models_count = CarModel.objects.all().count()
    services = Service.objects.all()
    services_count = Service.objects.all().count()

    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1

    context = {
        'registered_cars_models_count': registered_cars_models_count,
        'services': services,
        'services_count': services_count,
        'num_visits': num_visits,
    }
    return render(request, 'index.html', context)


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
    if request.method == "POST":
        comment = request.POST['comment']
        review = OrderListReview(order_list=order_list_id, reviewer=request.user, content=comment)
        review.save()
        messages.info(request, f'Review posted successfully')
        print(review)
        return redirect('specific_order', order_list.order_list_id_id)

    return render(request, 'specific_order.html', context)

def search_car(request):
    query = request.GET.get('query')
    search_results = Car.objects.filter(Q(client__icontains=query)
                                        | Q(car_model__car_model__icontains=query)
                                        | Q(car_model__brand__icontains=query)
                                        | Q(plate_number__icontains=query)
                                        | Q(vin_number__icontains=query))
    return render(request, 'search_cars.html', {'cars': search_results, 'query': query})

@login_required(login_url='login')
def user_orders(request):
    user = request.user
    try:
        user_order_lists = OrderList.objects.filter(user_order=request.user)#.filter(order_status__exact='r').order_by('due_back')
    except OrderList.DoesNotExist:
        user_order_lists = None
    print(user_order_lists)
    context = {
        'user': user,
        'user_order_lists': user_order_lists,
    }
    return render(request, 'user_order.html', context)

@csrf_protect
def register(request):
    if request.method == "POST":
        # pasiimame reikšmes iš registracijos formos
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        # tikriname, ar sutampa slaptažodžiai
        if password == password2:
            # tikriname, ar neužimtas username
            if User.objects.filter(username=username).exists():
                messages.error(request, f'Vartotojo vardas {username} užimtas!')
                return redirect('register')
            else:
                # tikriname, ar nėra tokio pat email
                if User.objects.filter(email=email).exists():
                    messages.error(request, f'Vartotojas su el. paštu {email} jau užregistruotas!')
                    return redirect('register')
                else:
                    # jeigu viskas tvarkoje, sukuriame naują vartotoją
                    User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
                    messages.info(request, f'Vartotojas {username} užregistruotas!')
                    return redirect('login')
        else:
            messages.error(request, 'Slaptažodžiai nesutampa!')
            return redirect('register')
    return render(request, 'registration/register.html')


