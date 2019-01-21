from django.contrib import admin
from food_journal.models import IngredientsMeta, MealMeta, MealInstance, IngredientInstance

# Register your models here.
admin.site.register(MealMeta)


class IngredientsInline(admin.TabularInline):
    model = IngredientInstance


@admin.register(IngredientsMeta)
class IngredientsAdmin(admin.ModelAdmin):
    list_display = ['ingredient_name']
    fields = ['ingredient_name']
    inlines = [IngredientsInline]


@admin.register(MealInstance)
class MealsAdmin(admin.ModelAdmin):
    list_display = ('meal_name', 'rating')
    fields = ['meal_name', 'rating']
    inlines = [IngredientsInline]
