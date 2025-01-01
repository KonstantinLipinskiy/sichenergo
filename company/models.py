from django.db import models

class Presentation(models.Model):
	title = models.CharField(max_length=155, verbose_name='Презентація')
	image = models.ImageField(upload_to='present/', verbose_name='Зображення')
	description = models.CharField(max_length=255, verbose_name='')
	file_present = models.FileField(upload_to='ol/', verbose_name="Файл для скачування")

	def __str__(self):
		return self.title
	
	class Meta:
		verbose_name = 'Презентацію'
		verbose_name_plural = 'Презентація'