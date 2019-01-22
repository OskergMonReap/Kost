from django.test import SimpleTestCase
from django.urls import reverse, resolve

from food_journal.views import food_journal_view


class TestUrls(SimpleTestCase):

    def test_food_journal_url(self):
        url = reverse('food')
        self.assertEqual(resolve(url).func, food_journal_view)
