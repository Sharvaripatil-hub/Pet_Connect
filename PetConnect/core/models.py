from django.db import models
from django.contrib.auth.models import User

class Pet(models.Model):
    """
    Represents a pet available for adoption.
    Attributes:
        name (CharField): The name of the pet.
        breed (CharField): The breed of the pet.
        age (IntegerField): The age of the pet.
        description (TextField): A description of the pet.
        adopted (BooleanField): Indicates whether the pet has been adopted (default is False).
    Methods:
        __str__(): Returns the name of the pet as its string representation.
    """
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    age = models.IntegerField()
    description = models.TextField()
    adopted = models.BooleanField(default=False)

    def __str__(self):
        return self.name