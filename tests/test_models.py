from django.test import TestCase
from food_journal.models import (
    IngredientInstance,
    IngredientsMeta,
    MealInstance,
    MealMeta,
)


class TestModels(TestCase):
    def setUp(self):

        self.ingredient_a = IngredientsMeta.objects.create(ingredient_name='potatoes')
        self.ingredient_b = IngredientsMeta.objects.create(ingredient_name='beef')
        self.meal_a = MealMeta.objects.create(meal_name='Beef Potato Medley')
        self.meal_a_instance = MealInstance.objects.create(
            timestamp=6,
            meal=self.meal_a,
            rating=7,
        )
        self.meal_a_instance = MealInstance.objects.create(
            timestamp=6,
            meal=self.meal_a,
            rating=7,
        )
        self.ingredient_a_instance = IngredientInstance.objects.create(
            ingredient_name=self.ingredient_a,
            prep_method='baked',
            rating=7,
            meal_details=self.meal_a_instance,
        )
        self.ingredient_b_instance = IngredientInstance.objects.create(
            ingredient_name=self.ingredient_b,
            prep_method='boiled',
            rating=6,
            meal_details=self.meal_a_instance,
        )

    def test_ingredient_meta(self):
        self.assertEqual(self.ingredient_a.ingredient_name, 'potatoes')
        self.assertEqual(self.ingredient_b.ingredient_name, 'beef')

    def test_meal_meta(self):
        self.assertEqual(self.meal_a.meal_name, 'Beef Potato Medley')

    def test_meal_instance(self):
        self.assertEqual(self.meal_a_instance.rating, 7)
        self.assertEqual(self.meal_a_instance.meal.meal_name, 'Beef Potato Medley')

    def test_ingredient_instances(self):
        # Ingredient A
        self.assertEqual(self.ingredient_a_instance.prep_method, 'baked')
        self.assertEqual(self.ingredient_a_instance.rating, 7)
        self.assertEqual(self.ingredient_a_instance.ingredient_name.ingredient_name, 'potatoes')
        self.assertEqual(self.ingredient_a_instance.meal_details.meal.meal_name, 'Beef Potato Medley')
        # Ingredient B
        self.assertEqual(self.ingredient_b_instance.prep_method, 'boiled')
        self.assertEqual(self.ingredient_b_instance.rating, 6)
        self.assertEqual(self.ingredient_b_instance.ingredient_name.ingredient_name, 'beef')
        self.assertEqual(self.ingredient_b_instance.meal_details.meal.meal_name, 'Beef Potato Medley')
