from django.db import models
from django.contrib.auth.models import User


# Форум
class ForumPost(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержимое")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="forum_posts")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class ForumPostLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(ForumPost, on_delete=models.CASCADE, related_name="likes")
    is_like = models.BooleanField(default=True)  # True = лайк, False = дизлайк

    class Meta:
        unique_together = ('user', 'post')

    def __str__(self):
        return f"{self.user.username} -> {self.post.title} ({'👍' if self.is_like else '👎'})"


# Скарги
class Complaint(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    image = models.ImageField(upload_to='complaints/', blank=True, null=True)
    seriousness = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    complaint = models.ForeignKey(
        Complaint, on_delete=models.CASCADE,
        related_name="likes", null=True, blank=True
    )
    is_like = models.BooleanField(default=True)

    class Meta:
        unique_together = ('user', 'complaint')

