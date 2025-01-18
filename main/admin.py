from django.contrib import admin
from .models import MainInfo, MainItem

@admin.register(MainInfo)
class MainInfoAdmin(admin.ModelAdmin):
	list_display = ('title', 'image', 'name', 'description')

@admin.register(MainItem)
class MainItemAdmin(admin.ModelAdmin):
	list_display = ('title', 'image', 'detail_url')