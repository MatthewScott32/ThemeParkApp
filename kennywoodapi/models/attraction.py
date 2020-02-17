from django.db import models
from .parkarea import ParkArea

class Attraction(models.Model):

    name = models.CharField(max_length=50)
    area = models.ForeignKey(ParkArea, on_delete=models.DO_NOTHING, related_name="attractions")

    class Meta:
        ordering = ("area",)

    def __str__(self):
        return self.name
