from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """
    Model representing an address.

    Attributes:
        number (PositiveIntegerField): The number part of the address.
        street (CharField): The street name.
        city (CharField): The city name.
        state (CharField): The state abbreviation.
        zip_code (PositiveIntegerField): The ZIP code.
        country_iso_code (CharField): The ISO country code.
    """

    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    def __str__(self):
        """
        String representation of the address.

        Returns:
            str: The formatted address as a string.
        """
        return f'{self.number} {self.street}'

    class Meta:
        """
        Meta options for the Address model.

        Attributes:
            verbose_name_plural (str): The plural name for the model in the admin interface.
        """
        verbose_name_plural = "addresses"


class Letting(models.Model):
    """
    Model representing a letting.

    Attributes:
        title (CharField): The title of the letting.
        address (OneToOneField): The address associated with the letting.
    """

    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        """
        String representation of the letting.

        Returns:
            str: The title of the letting.
        """
        return self.title
