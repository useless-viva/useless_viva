from django.db import models


class Question(models.Model):
    que = models.CharField(max_length=200)
    answer1 = models.TextField()
    answer2 = models.TextField()
    page = models.IntegerField()