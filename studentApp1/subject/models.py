from django.db import models


class Subject(models.Model):
    name = models.CharField(max_length=100)
    subCode = models.CharField(max_length=3)


    def __str__(self):
        return self.name
