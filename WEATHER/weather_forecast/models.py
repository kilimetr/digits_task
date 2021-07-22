from django.db import models



# Create your models here.
class Weather_Update(models.Model):
	date    = models.DateField(blank = True, null = True)
	country = models.CharField(max_length = 2, blank = True, null = True)

	def __str__(self):
		return self.country

	class Meta:
		verbose_name = "Country Weather"
		verbose_name_plural = "Countries Weather"
