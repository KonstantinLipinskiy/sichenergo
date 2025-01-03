from django.template.context_processors import media
from django.urls import path

from company import views

app_name='company'

urlpatterns = [
	path('', views.company, name='company'),
	path('about/', views.about, name='about'),
	path('documents/', views.documents, name='documents'),
	path('reviews/', views.reviews, name='reviews'),
]