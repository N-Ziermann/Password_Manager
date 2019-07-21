from django.db import models

# Create your models here.
class User(models.Model):
	mail = models.EmailField(blank=False, unique=True)
	password = models.CharField(max_length=100)
	data = models.TextField()	#encrypted array in string format
	def __str__(self):
		return self.mail