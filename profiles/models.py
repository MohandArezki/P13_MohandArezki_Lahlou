from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Model representing a user profile.

    Attributes:
        user (User): One-to-one relationship with the User model.
        favorite_city (str): The user's favorite city (optional).
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        """
        String representation of the Profile object.

        Returns:
            str: The username of the associated user.
        """
        return self.user.username
