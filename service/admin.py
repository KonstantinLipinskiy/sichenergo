from django.contrib import admin

from .models import ServiceInform

@admin.register(ServiceInform)
class ServiceInform(admin.ModelAdmin):
	list_display = ('title', 'video', 'name', 'description')


