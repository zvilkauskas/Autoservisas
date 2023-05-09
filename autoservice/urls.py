from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('registered_car_models/', views.CarListView.as_view(), name='registered_car_models'),
    path('registered_car_models/<int:car_id>', views.specific_car, name='specific_car'),
    path('services/', views.services, name='services'),
    path('orders/', views.orders, name='orders'),
    path('orders/<int:order_list_id>', views.specific_order, name='specific_order'),
    path('search_car/', views.search_car, name='search_car'),
    path('accounts/', include('django.contrib.auth.urls')),
]
