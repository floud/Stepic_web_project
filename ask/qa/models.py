from django.db import models
from django.contrib.auth.models import User


# Create your models here

class DjangoUser(User):
    pass

class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(blank=True)
    rating = models.IntegerField()
    author = models.ForeignKey(DjangoUser, null=False, on_delete=models.DO_NOTHING,related_name='question_author')
    likes = models.ManyToManyField(DjangoUser)


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(blank=True)
    question = models.ForeignKey(Question, null=False, on_delete=models.CASCADE)
    author = models.ForeignKey(DjangoUser, null=False, on_delete=models.DO_NOTHING)
