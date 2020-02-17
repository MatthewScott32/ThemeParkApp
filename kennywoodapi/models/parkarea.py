from django.db import models


class ParkArea(models.Model):
    name = models.CharField(max_length=50)
    theme = models.CharField(max_length=50)

    class Meta:
        ordering = ("theme",)

    def __str__(self):
        return self.name
