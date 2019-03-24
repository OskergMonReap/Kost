from django import forms

from food_journal.config.options import RATINGS, PREP_METHODS


class MealForm(forms.Form):
    meal_name = forms.CharField(max_length=30)
    rating = forms.ChoiceField(choices=RATINGS)
    prep_method = forms.ChoiceField(choices=PREP_METHODS)
    # TODO research and implement field for ingredients, similar to models
