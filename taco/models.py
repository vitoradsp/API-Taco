from django.db import models


class Alimento(models.Model):    
    name = models.CharField(max_length=255, null=True)
    kcal = models.IntegerField()
    protein = models.IntegerField(null=True, default=0)
    fat = models.IntegerField(null=True, default=0)
    carbo = models.IntegerField(null=True, default=0)
    def __str__(self):
        return f"{self.name} {self.protein} {self.fat} {self.carbo}"

    class Meta:
        verbose_name_plural = "Alimentos"

