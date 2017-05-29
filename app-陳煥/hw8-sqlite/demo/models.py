from django.db import models

# Create your models here.
class Fruit(models.Model):
	name = models.CharField(max_length=20)
	price = models.DecimalField(max_digits=6, decimal_places=0)
	def __str__(self):
		return self.name 