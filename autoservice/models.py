from django.db import models
from django.utils import timezone
import datetime


class CarModel(models.Model):
    car_model_id = models.AutoField(primary_key=True)
    brand = models.CharField("Brand", max_length=100)
    car_model = models.CharField("Car model", max_length=100)
    production_year = models.DateField("Made on: ", null=True)
    engine = models.CharField("Engine", max_length=100)

    def __str__(self):
        return f"{self.brand} - {self.car_model}"

    class Meta:
        verbose_name = 'Car Model'
        verbose_name_plural = 'Car Models'


class Car(models.Model):
    car_id = models.AutoField(primary_key=True)
    car_model = models.ForeignKey(CarModel, on_delete=models.SET_NULL, null=True)
    plate_number = models.CharField("Plate number", max_length=20)
    vin_number = models.CharField("VIN", max_length=17)
    client = models.CharField("Client", max_length=100)

    def __str__(self):
        return f"{self.client} - {self.car_model} - {self.plate_number} - {self.vin_number}"

    class Meta:
        verbose_name = 'Car'
        verbose_name_plural = 'Cars'


class Service(models.Model):
    service_id = models.AutoField(primary_key=True)
    service_name = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.service_name}"

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'


class ServicePrice(models.Model):
    service_price_id = models.AutoField(primary_key=True)
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True)
    cars = models.ManyToManyField(CarModel)
    price = models.FloatField("Price")

    def __str__(self):
        return f"{self.service} - {self.price}"

    class Meta:
        verbose_name = 'Service price'
        verbose_name_plural = 'Service prices'


# Uzsakymas
class OrderList(models.Model):
    """Order List which is connected to an order. Representing the visit to an autoservice shope and the total order placed."""
    order_list_id = models.AutoField(primary_key=True)
    order_date = models.DateTimeField(default=timezone.now)
    car = models.ForeignKey(Car, on_delete=models.SET_NULL, null=True)
    total_price = models.FloatField()


    def __str__(self):
        return f"{self.car} - {self.order_date} - {self.total_price}"

    class Meta:
        verbose_name = 'Order List'
        verbose_name_plural = 'Order Lists'


# TODO - prideti manytomany field i admina per atskira method
# Uzsakymo eilute
class Order(models.Model):
    """Order which is connected to an order list. Representing one service/thing bought."""
    order_id = models.AutoField(primary_key=True)
    order_list_id = models.ForeignKey(OrderList, on_delete=models.SET_NULL, null=True)
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField()
    price = models.FloatField()

    def __str__(self):
        return f"{self.order_list_id} - {self.service} - {self.quantity} - {self.price}"

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'


# order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
# service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True)
# quantity = models.IntegerField()