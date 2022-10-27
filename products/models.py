from django.db import models

# Create your models here.
class product(models.Model):

    name = models.CharField(max_length=30)
    price = models.IntegerField()
    stock = models.IntegerField()
    description = models.CharField(max_length=150)


    def __str__(self) -> str:
        return self.name