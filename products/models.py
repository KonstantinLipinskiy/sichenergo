from pyexpat import model
from django.db import models
from tabnanny import verbose

class TransformItem(models.Model):
	name = models.CharField(max_length=255, verbose_name='Серія')
	image = models.ImageField(upload_to='media/', verbose_name='Зображення')
	detail_url = models.URLField(blank=True, null=True, verbose_name='Посилання')

	def __str__(self):
		return self.name
	
	class Meta:
		db_table= 'transform'
		verbose_name = 'Серію'
		verbose_name_plural = 'Серія трансформатора'

class InformTransform(models.Model):
	title = models.CharField(max_length=150, verbose_name='Опитовий лист')
	video = models.FileField(upload_to='video/', verbose_name="Відео", blank=True, null=True)
	description = models.TextField(verbose_name='Опис', blank=True)
	file_ol = models.FileField(upload_to='ol/', verbose_name="Файл для скачування")

	def __str__(self):
		return self.title
	
	class Meta:
		verbose_name = "Опитувальний лист"
		verbose_name_plural = "Опитувальні листи"
	
class TransformTm(models.Model):
	name = models.CharField(max_length=255, verbose_name='Потужність трансформаторів ТМ та ТМЖ')
	image = models.ImageField(upload_to='img_tm/', verbose_name='Креслення трансформаторів ТМ та ТМЖ')
	file_tm = models.FileField(upload_to='drawing_tm/', verbose_name='Скачати креслення трансформаторів ТМ та ТМЖ')

	def __str__(self):
		return self.name
	
	class Meta:
		verbose_name = "Трансформатор ТМ та ТМЖ"
		verbose_name_plural = "Трансформатори ТМ та ТМЖ"