from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
	context = {
		"title": "Головна", 
		}

	return render(request, "main/index.html", context)