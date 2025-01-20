from django.db import models
from cloudinary.models import CloudinaryField
from cloudinary_storage.storage import RawMediaCloudinaryStorage

class NewsItem(models.Model):
	title = models.CharField(max_length=255, verbose_name='Заголовок')
	content = models.TextField(verbose_name='Текст')
	CONTENT_TYPE_CHOICES = [
		('image', 'Зображення'),
		('video', 'Відео'),
	]
	content_type = models.CharField( max_length=10, choices=CONTENT_TYPE_CHOICES, verbose_name='Тип контенту' ) # Использование CloudinaryField для загрузки файлов 
	content_file = CloudinaryField( resource_type='auto', default='static/deps/img/trans.png', verbose_name='Файл контента')
	region= models.CharField(max_length=255, verbose_name='Регіон')
	heading= models.CharField(max_length=255, verbose_name='Рубрика')
	created_at= models.DateTimeField(auto_now_add=True, verbose_name='Дата створення')

	def __str__(self):
		return self.title
	
	class Meta:
		db_table= 'news'
		verbose_name = 'Новину'
		verbose_name_plural = 'Новини'
		ordering = ['-created_at']
	
