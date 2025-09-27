from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

class Profile(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField(validators=[MinValueValidator(14), MaxValueValidator(100)])

class Story(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='stories/')
    created_at = models.DateTimeField(auto_now_add=True)

    def str(self):
        return self.title

    class Meta:
        verbose_name = "Історія"
        verbose_name_plural = "Історії"
        ordering = ['-created_at']  # новые сначала
