from django.urls import path
from . import views

urlpatterns = [
    path('', views.food_journal_view, name='food')
]
