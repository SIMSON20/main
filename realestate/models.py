from django.db import models
from django.core.urlresolvers import reverse

School = 'school.School'


# Create your models here.
class Company(models.Model):
	# Characteristics about a Real Estate company
	name = models.CharField(max_length=60)
	
	# default_school is used to center the map
	default_school = models.ForeignKey(School, null=True, blank=True)

	def get_absolute_url(self):
		return reverse('real-estate-search', kwarg={'slug':slugify(self.name)})

	def __str__(self):
		return self.name