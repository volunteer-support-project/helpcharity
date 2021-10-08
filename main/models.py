from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User


class Contact(User, models.Model):
    phone_number = PhoneNumberField(blank=True)
    special_data = models.CharField(max_length=255)  # Типа: "О себе", хз зачем, но так обычно делают
    photo = models.ImageField(upload_to='', null=True)  # Обсудить, как и где хранить фото пользователя

    def __str__(self):
        return self.username


class Volunteer(Contact):
    pass


class Inspector(Contact):
    token = models.CharField(max_length=8)
    organizer = models.ManyToManyField('Organization')


class Organization(Contact):
    title = models.CharField(max_length=64)
    tags = models.ManyToManyField('Tag', null=True)
    venue = models.CharField(max_length=128)  # Подключать геолокацию слишком сложно

    def __str__(self):
        return self.title


class Event(Contact):
    title = models.CharField(max_length=64)
    time = models.DateTimeField()
    organizer = models.ManyToManyField('Organization')
    agreed = models.BooleanField(False)

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=128)

    def __str__(self):
        return self.name
