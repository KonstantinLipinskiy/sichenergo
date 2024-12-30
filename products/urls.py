from django.template.context_processors import media
from django.urls import path

from products import views

app_name='products'

urlpatterns = [
	path('', views.products, name='products'),
	path('transformers/', views.transformers, name='transformers'),
	path('transformers/tm/', views.transformers_tm, name='tm'),
	path('transformers/tmg/', views.transformers_tmg, name='tmg'),
	path('transformers/tmz/', views.transformers_tmz, name='tmz'),
	path('transformers/yz/', views.transformers_yz, name='yz'),
	path('ktp/', views.ktp, name='ktp'),
	]