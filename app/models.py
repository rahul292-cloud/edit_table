from django.db import models


class Test(models.Model):
    name=models.CharField(max_length=200)
    result=models.CharField(max_length=200)
    def __str__(self):
        return self.name