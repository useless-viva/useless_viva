from django.db import models


class User(models.Model):
    username = models.CharField(max_length=50)
    result = models.CharField(max_length=50)
    result1 = models.IntegerField(default=0)
    result2 = models.IntegerField(default=0)
    result3 = models.IntegerField(default=0)
    result4 = models.IntegerField(default=0)