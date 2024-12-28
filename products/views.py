from django.shortcuts import render
from .models import *

def products(request):
	return render(request)

def transformers(request):
	series = TransformItem.objects.all()
	context = {
		"title" : "Cилові масляні трансформатори з класами напруги до 35 кВ та потужністю до 2500 кВА (ТМ, ТМГ, ТМЗ, ТМЖГ)",
		"series": series,
	}
	return render(request, "products/transformers.html", context)
