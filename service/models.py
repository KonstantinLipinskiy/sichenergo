from django.db import models
from cloudinary.models import CloudinaryField
from cloudinary_storage.storage import RawMediaCloudinaryStorage

class ServiceInform(models.Model):
	title = models.CharField(max_length=155, verbose_name='Інформація', blank=True, null=True)
	video = models.FileField(upload_to='videos/', blank=True, null=True, storage=RawMediaCloudinaryStorage(), verbose_name='Відео')
	name = models.CharField(max_length=155, verbose_name='Назва події', blank=True, null=True)
	description = models.TextField(verbose_name='Опис', blank=True, null=True)

	def __str__(self):
		return self.name
	
	class Meta:
		verbose_name = 'Подія'
		verbose_name_plural = 'Події'
