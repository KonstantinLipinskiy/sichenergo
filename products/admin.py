from django.contrib import admin
from .models import *

@admin.register(TransformItem)
class TransformItemAdmin(admin.ModelAdmin):
	list_display = ('name', 'image', 'detail_url')


