from django.db import models

class Result(models.Model):
    image = models.ImageField(upload_to = "result/", blank=True, null=True)
    body =  models.TextField()


