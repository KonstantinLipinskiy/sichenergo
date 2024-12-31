from django.db import models

class NewsItem(models.Model):
	title = models.CharField(max_length=255, verbose_name="Заголовок")
	content = models.TextField(verbose_name="Текст")
	CONTENT_TYPE_CHOICES = [
		('image', 'Зображення'),
		('video', 'Відео'),
	]
	content_type = models.CharField(
		max_length = 10,
		choices = CONTENT_TYPE_CHOICES,
		verbose_name = "Тип контенту"
	)
	content_file = models.FileField(
		upload_to ='media/',
		verbose_name ="Файл контента" 
	)
	region= models.CharField(max_length=255, verbose_name="Регіон")
	heading= models.CharField(max_length=255, verbose_name='Рубрика')
	created_at= models.DateTimeField(auto_now_add=True, verbose_name="Дата створення")

	def __str__(self):
		return self.title
	
	class Meta:
		db_table= 'news'
		verbose_name = 'Новину'
		verbose_name_plural = 'Новини'
		ordering = ['-created_at']
	
