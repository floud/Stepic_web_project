from django.db import models
from django.contrib.auth.models import User

# Create your models here

class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(blank=True)
    rating = models.IntegerField()
    author = User()
    likes = [User]

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(blank=True)
    question = models.ForeignKey(Question, null=False, on_delete=models.CASCADE())
    author = User()

