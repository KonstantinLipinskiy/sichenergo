from django.http import HttpResponse
from django.shortcuts import render

from .models import MainInfo, MainItem


def index(request):
	items = MainItem.objects.all()
	info = MainInfo.objects.first()

	context = {
		'title': 'Головна',
		'items': items,
		'info': info,
		}

	return render(request, 'main/index.html', context)