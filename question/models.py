from django.db import models


class Question(models.Model):
    que = models.CharField(max_length=200)
    answer1 = models.CharField(max_length=50)
    answer2 = models.CharField(max_length=50)
    page = models.IntegerField()