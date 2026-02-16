from django.db import models

class Bot(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Scenario(models.Model):
    bot = models.ForeignKey(Bot, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

ROLE_CHOICES = (
    ('system', 'System'),
    ('user', 'User'),
    ('assistant', 'Assistant'),
)

class Step(models.Model):
    scenario = models.ForeignKey(Scenario, on_delete=models.CASCADE)
    order = models.IntegerField()
    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)