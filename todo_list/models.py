from django.db import models

# Create your models here.

class Task(models.Model):
  LEVEL_CHOICES=[
    ('faible', 'Faible'),
    ('moyen', 'Moyen'),
    ('urgent','Urgent')
  ]
  title=models.CharField(max_length=255)
  description=models.TextField(max_length=255)
  completed=models.BooleanField(default=False)
  created_at=models.DateTimeField(auto_now_add=True)
  priority=models.CharField(max_length=80, default='faible',choices=LEVEL_CHOICES)

  def __str__(self):
    return self.title