from django.db import models

# Create your models here.
class User(models.Model):
	mail = models.EmailField(unique=True, max_length=100)
	password = models.CharField(max_length=100)
	data = models.TextField()	#encrypted array in string format
	def __str__(self):
		return self.mail
# work with this : https://www.youtube.com/watch?v=b8RpVs7bSgo