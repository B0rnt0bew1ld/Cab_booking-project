from django.db import models

# Create your models here.
class Station(models.Model):
    pin_code = models.IntegerField()
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} ({self.pin_code})"

class Cabs(models.Model):
    pick = models.ForeignKey(Station, on_delete= models.CASCADE, related_name="departures")
    drop = models.ForeignKey(Station, on_delete=models.CASCADE, related_name="arrivals")
    cost = models.IntegerField()

    def __str__(self):
        return f"{self.pick} to {self.drop} costs Rs {self.cost}."

class Passanger(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    cabs = models.ManyToManyField(Cabs, blank = True, related_name="passangers")

    def __str__(self):
        return f"{self.first} {self.last}"    