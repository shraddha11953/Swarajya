from django.db import models
from django.contrib.auth.models import User

# CATEGORY choices
CATEGORY_CHOICES = [
    ('Food', 'Food'),
    ('Clothes', 'Clothes'),
    ('Education', 'Education'),
    ('Shelter', 'Shelter'),
    ('Other', 'Other'),
]

# 🔹 Help Offer Model
class HelpOffer(models.Model):
    HELP_TYPES = [
        ('Food', 'Food'),
        ('Clothes', 'Clothes'),
        ('Education', 'Education'),
        ('Money', 'Money'),
        ('Other', 'Other'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    help_type = models.CharField(max_length=50, choices=HELP_TYPES)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.help_type}"


# 🔹 Help Request Model
class HelpRequest(models.Model):
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    image = models.ImageField(upload_to='help_requests/', blank=True, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
