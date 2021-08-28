from django.urls import path
from . import views

app_name = "pizzas"

urlpatterns = [
    path("", views.index, name="index"),
    path("pizzas/", views.list_of_pizzas, name = "list_of_pizzas"),
    path("pizzas/<int:pizza_id>/", views.each_pizza, name= "each_pizza"),
]