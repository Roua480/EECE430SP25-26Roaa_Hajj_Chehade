from django.db import models


class VoleyPlayer(models.Model):
    name = models.CharField(max_length=100)
    dateJoined = models.DateField()
    position = models.CharField(max_length=50)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    contactPerson = models.CharField(max_length=100)

    def __str__(self):
        return self.name