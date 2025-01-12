from django.urls import path

from entrance import views

app_name='entrance'

urlpatterns = [
	 path('', views.entrance, name='entrance')
]