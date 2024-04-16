from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import Profile


class ProfilesTest(TestCase):
    """
    Test case for the Profiles app.
    """

    def setUp(self):
        """
        Set up the test data before each test method.
        """
        # Create a User instance for testing
        self.user = User.objects.create_user(
            username="UserTest",
            password="password123",
            email="test@email.com"
        )
        # Create a Profile instance linked to the user
        self.profile = Profile.objects.create(user=self.user, favorite_city="MyFavoriteTestCity")

    def test_profiles_index(self):
        """
        Test the index view of the Profiles app.
        """
        # Check if the index page returns a status code 200 and if the title is
        # present in the content
        url = reverse('profiles:index')
        expected_html = '<a href="/profiles/UserTest/">UserTest</a>'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, expected_html, html=True)

    def test_profile_detail(self):
        """
        Test the profile detail view of the Profiles app.
        """
        # Check if the profile detail page returns a status code 200 and
        # if the username is present in the content
        url = reverse('profiles:profile', args=["UserTest"])
        expected_html = "<title>UserTest</title>"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, expected_html)

    def test_profiles_models_str(self):
        """
        Test the __str__ method of the Profile model.
        """
        # Check if the string representation of the profile matches
        # the username of the associated user
        self.assertEqual(str(self.profile), self.user.username)
