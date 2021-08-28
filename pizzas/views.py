from django.shortcuts import render
from . models import Pizza, Topping

# Create your views here.

def index(request):
    return render(request, "pizzas/index.html")

def list_of_pizzas(request):
    pizzas = Pizza.objects.all()
    context = {'pizzas': pizzas}
    return render(request, "pizzas/list_of_pizzas.html", context)

def each_pizza(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.topping_set.all()
    context = {"pizza" : pizza, "toppings" : toppings}
    return render(request, "pizzas/each_pizza.html", context)