from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class FreedomPost(models.Model):
    CATEGORY_CHOICES = [
        ('politics', 'Politics'),
        ('education', 'Education'),
        ('women', 'Women Safety'),
        ('judiciary', 'Judiciary'),
        ('corruption', 'Corruption'),
        ('police', 'Police Injustice'),
        ('farmer', 'Farmer Rights'),
        ('child', 'Child Rights'),
        ('public', 'Public Issues'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    content = models.TextField()
    is_anonymous = models.BooleanField(default=False)
    support_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)
    support = models.IntegerField(default=0)


    def display_user(self):
        return "Anonymous" if self.is_anonymous else self.user.username

    def __str__(self):
        return f"{self.display_user()} - {self.category}"

