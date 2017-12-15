from __future__ import unicode_literals
from django.db import models
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


# Create your models here.

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['name']) < 3:
            errors["name"] = "Name should be more than 3 characters"
        elif  not postData['name'].isalpha():
            errors["name"] = "Name can only be alphabet"
        if len(postData['alias']) < 3:
            errors["alias"] = "Alias should be more than 3 characters"
        elif  not postData['name'].isalpha():
            errors["name"] = "Name can only be alphabet"
        return errors

class User(models.Model):
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    objects = UserManager()