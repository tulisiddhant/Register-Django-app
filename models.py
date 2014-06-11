from django.db import models

# Create your models here.
class Person(models.Model):
	f_name = models.CharField(max_length=20)
	l_name = models.CharField(max_length=20)
	age = models.IntegerField(default=10)

	def __unicode__(self):
		return self.f_name

class Book(models.Model):
	person = models.ForeignKey(Person)
	name = models.CharField(max_length=20)
	author = models.CharField(max_length=20)
	
	def __unicode__(self):
		return self.name
