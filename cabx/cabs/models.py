from django.db import models

# Create your models here.
class Station(models.Model):
    pin_code = models.IntegerField()
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"City name : {self.city} and Pincode : {self.pin_code}"

class Cabs(models.Model):
    pick = models.CharField(max_length=64)
    drop = models.CharField(max_length=64)
    cost = models.IntegerField()

    def __str__(self):
        return f"Your picking point : {self.pick}, dropping point : {self.drop} and cost : Rs {self.cost}."
    