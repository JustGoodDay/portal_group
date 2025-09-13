from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User




#модель форума


class ForumPost(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержимое")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="forum_posts")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Complaint(models.Model):
    SERIOUSNESS_CHOICES = [
        ('low', 'Низкая'),
        ('medium', 'Средняя'),
        ('high', 'Высокая'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="complaints")
    text = models.TextField(verbose_name="Текст жалобы")
    image = models.ImageField(upload_to="complaints/", blank=True, null=True, verbose_name="Фото")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата подачи")
    seriousness = models.CharField(max_length=10, choices=SERIOUSNESS_CHOICES, default="medium")

    def __str__(self):
        return f"Жалоба от {self.user.username} ({self.seriousness})"
