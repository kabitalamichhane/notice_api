from django.db import models


class Notice(models.Model):
    PRIORITY_CHOICES = [("low", "Low"), ("medium", "Medium"), ("high", "High")]

    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=50, blank=True)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default="medium")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]   # newest notice first

    def __str__(self):
        return self.title
