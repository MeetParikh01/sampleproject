from django.db import models
from django.contrib.auth.models import User

class DBform(models.Model):
	name=models.CharField(max_length = 100)
	date_time=models.DateTimeField(auto_now_add=True)
	weight=models.IntegerField()
	age=models.IntegerField()
	gender=models.CharField(max_length=6)
