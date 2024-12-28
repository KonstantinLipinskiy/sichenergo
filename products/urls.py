from django.template.context_processors import media
from django.urls import path

from products import views

app_name='products'

urlpatterns = [
	 path('', views.products, name='products'),
	 path('transformers/', views.transformers, name='transformers')
	]