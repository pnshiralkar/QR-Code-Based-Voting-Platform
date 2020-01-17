from django.db import models


class Vote(models.Model):
    IDNumber = models.CharField(max_length=11)
    photo1 = models.CharField(max_length=10, null=True)
    photo2 = models.CharField(max_length=10, null=True)
    photo3 = models.CharField(max_length=10, null=True)
    drawing1 = models.CharField(max_length=10, null=True)
    drawing2 = models.CharField(max_length=10, null=True)
    drawing3 = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.IDNumber

