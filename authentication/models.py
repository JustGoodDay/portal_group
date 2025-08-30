from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

class Profile(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField(validators=[MinValueValidator(14), MaxValueValidator(100)])

    photo = models.ImageField(blank=True)

class Group(models.Model):

    members = models.ManyToManyField(User)

class Diary(models.Model):

    group = models.ForeignKey(Group, on_delete=models.CASCADE)


class Grade(models.Model):

    Diary = models.ForeignKey(Diary, on_delete=models.CASCADE)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

