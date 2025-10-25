from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class CorruptionReport(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    date = models.DateTimeField(default=timezone.now)
    proof_image = models.ImageField(upload_to='corruption_proofs/', null=True, blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
