from django.test import TestCase
from django.urls import reverse
from .models import Address, Letting


class LettingsTest(TestCase):
    """
    Test case for the Lettings app.
    """

    def setUp(self):
        """
        Set up the test data before each test method.
        """
        # Creates instances of Address and Letting for testing
        self.address = Address.objects.create(
            number=2,
            street="Boulevard test 1",
            city="City 1",
            state="State1",
            zip_code=669988,
            country_iso_code="FRA"
        )
        self.letting = Letting.objects.create(title="Test Letting", address=self.address)

    def test_lettings_index(self):
        """
        Test the index view of the Lettings app.
        """
        # Checks if the index page returns a status code 200 and
        # if the title is present in the content
        response = self.client.get(reverse('lettings:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "<title>Lettings</title>")

    def test_letting_detail(self):
        """
        Test the letting detail view of the Lettings app.
        """
        # Checks if the letting detail page returns a status code 200
        # and if the title of the letting is present in the content
        response = self.client.get(reverse('lettings:letting', args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "<title>Test Letting</title>")

    def test_lettings_models_str(self):
        """
        Test the __str__ methods of the Address and Letting models.
        """
        # Checks if the string representation of the instances matches the expected format
        self.assertEqual(str(self.address), f'{self.address.number} {self.address.street}')
        self.assertEqual(str(self.letting), self.letting.title)
