from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


class Person(models.Model):
    """Model Person.Model for authenticate user and save personal dates."""
    DNI = 'DNI'
    FOREING_CARD = 'FC'
    OTHER = 'OTROS'
    IDENTITY_TYPE_CHOICES = (
        (DNI, 'DNI'),
        (FOREING_CARD, 'Canet de Extranjería'),
        (OTHER, 'Otros'),
    )
    first_name = models.CharField("Firs Name", max_length=50)
    last_name = models.CharField("Last Name", max_length=100)
    identity_type = models.CharField(
        max_length=15, choices=IDENTITY_TYPE_CHOICES, default=DNI)
    identity_num = models.CharField(
        max_length=20, error_messages={'unique': "eeeee ee"})
    photo = models.ImageField(upload_to='persons', blank=True, null=True)
    email = models.EmailField()
    birth_date = models.DateField(blank=True, null=True)

    updated_at = models.DateTimeField("Updated at", auto_now=True)
    created_at = models.DateTimeField("Created at", auto_now_add=True)

    class Meta:
        verbose_name = "Person"
        verbose_name_plural = "Persons"

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)


class User(AbstractUser):
    u"""Custom Users."""
    persona = models.OneToOneField(
        Person, verbose_name="Person", blank=True, null=True)
    updated_at = models.DateTimeField("Updated at", auto_now=True)
    created_at = models.DateTimeField("Created at", auto_now_add=True)
    objects = UserManager()

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        permissions = (
            ('list_user', 'Can list user'),
            ('get_user', 'Can get user'),
        )

    def __str__(self):
        return self.username
