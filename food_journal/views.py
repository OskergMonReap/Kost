from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import IngredientInstance, MealInstance, IngredientsMeta, MealMeta

# Create your views here.


def food_journal_view(request):
    food_items = MealInstance.objects.all()
    template = loader.get_template('home.html')
    context = {
        'food_items': food_items,
    }
    return HttpResponse(template.render(context, request))


def food_listings(request):
    food_items = MealInstance.objects.all()
    return HttpResponse(content=food_items)
