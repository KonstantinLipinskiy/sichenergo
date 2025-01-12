from django.db import models

class ServiceInform(models.Model):
	title = models.CharField(max_length=155, verbose_name='Інформація', blank=True, null=True)
	video = models.FileField(upload_to='video/', verbose_name='Відео', blank=True, null=True)
	name = models.CharField(max_length=155, verbose_name='Назва події', blank=True, null=True)
	description = models.TextField(verbose_name='Опис', blank=True, null=True)

	def __str__(self):
		return self.name
	
	class Meta:
		verbose_name = 'Подія'
		verbose_name_plural = 'Події'
