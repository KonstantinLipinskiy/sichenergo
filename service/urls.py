from django.template.context_processors import media
from django.urls import path

from service import views

app_name='service'

urlpatterns = [
	path('', views.service, name='service'),
	]