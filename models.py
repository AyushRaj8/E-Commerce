from django.db import models

# Create your models here.
class Customer(models.Model):
	name=models.CharField(max_length=30)
	email=models.CharField(max_length=50)
	password=models.CharField(max_length=20)
	contact=models.CharField(max_length=20)
	city=models.CharField(max_length=30)
	address=models.CharField(max_length=30)
	class Meta:
		db_table="Customer"

