from django.contrib import admin
from food_journal.models import IngredientsMeta, MealMeta, MealInstance, IngredientInstance


class IngredientsInline(admin.TabularInline):
    model = IngredientInstance


class MealsInline(admin.TabularInline):
    model = MealInstance


@admin.register(IngredientsMeta)
class IngredientsAdmin(admin.ModelAdmin):
    list_display = ['ingredient_name']
    fields = ['ingredient_name']
    inlines = [IngredientsInline]


@admin.register(MealInstance)
class MealsAdmin(admin.ModelAdmin):
    list_display = ('meal', 'rating')
    fields = ['meal', 'rating']
    inlines = [IngredientsInline]


@admin.register(MealMeta)
class MealMetaAdmin(admin.ModelAdmin):
    list_display = ['meal_name']
    fields = ['meal_name']
    inlines = [MealsInline]
