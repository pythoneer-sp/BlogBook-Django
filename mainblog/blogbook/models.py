from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Blog(models.Model):
    CATEGORY_CHOICES = [
        ('tech', 'Technology'),
        ('health', 'Health'),
        ('lifestyle', 'Lifestyle'),
        ('travel', 'Travel'),
    ]
    title = models.CharField(max_length=100)
    content = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='tech')
    user = models.ForeignKey(User, on_delete=models.CASCADE) #When the referenced object is deleted, also delete the objects that have references to it (when you remove a blog post for instance, you might want to delete comments as well). SQL equivalent
    photo = models.ImageField(upload_to='blog_photos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.title}"