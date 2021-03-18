from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Posts(models.Model):
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    station = models.CharField(max_length=64)
    price = models.FloatField(max_length=4,default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)
    updates_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
