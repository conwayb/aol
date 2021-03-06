from django.core.urlresolvers import reverse
from django.test import TestCase


class HomeTest(TestCase):
    # just make sure the views return a 200
    def test_homepage(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
