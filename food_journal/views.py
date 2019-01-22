from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def food_journal_view(request):
    return HttpResponse("The view in food_journal is working!")
