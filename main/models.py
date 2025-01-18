from django.db import models

class MainInfo(models.Model):
	title = models.CharField(max_length=155, verbose_name='Головна Інформація')
	image = models.ImageField(upload_to='main/', verbose_name='Зображення')
	name = models.CharField(max_length=155, verbose_name='Короткий опис')
	description = models.TextField(verbose_name='Опис')

	def __str__(self):
		return self.title
	
	class Meta:
		verbose_name = 'Інформацію'
		verbose_name_plural = 'Інформація'

class MainItem(models.Model):
	title = models.CharField(max_length=155, verbose_name='Головна Назва блоку')
	image = models.ImageField(upload_to='main/', verbose_name='Зображення')
	detail_url = models.URLField(blank=True, null=True, verbose_name='Посилання')

	def __str__(self):
		return self.title
	
	class Meta:
		verbose_name = 'Блок'
		verbose_name_plural = 'Блок'