from django.db import models
# from django.urls import reverse

from food_journal.config.options import RATINGS, PREP_METHODS


class IngredientsMeta(models.Model):
    ingredient_name = models.CharField(max_length=20)

    def __str__(self):
        return self.ingredient_name


class MealMeta(models.Model):
    meal_name = models.CharField(max_length=20)

    def __str__(self):
        return self.meal_name


class MealInstance(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    meal_name = models.ForeignKey('MealMeta', on_delete=models.SET_NULL, null=True)
    rating = models.IntegerField(choices=RATINGS)
    ingredients = models.ManyToManyField('IngredientInstance')

    def __str__(self):
        return f'{self.meal_name.meal_name} - {self.timestamp}'


class IngredientInstance(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    ingredient_name = models.ForeignKey('IngredientsMeta', on_delete=models.SET_NULL, null=True)
    rating = models.IntegerField(choices=RATINGS)
    prep_method = models.CharField(max_length=18, choices=PREP_METHODS)
    meal_details = models.ForeignKey('MealInstance', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.ingredient_name.ingredient_name} - {self.timestamp}'
