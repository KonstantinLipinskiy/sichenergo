from django.shortcuts import render
from .models import InformTransform, TransformItem, TransformTm

def products(request):
	return render(request)

def transformers(request):
	series = TransformItem.objects.all()
	inform = InformTransform.objects.first()
	context = {
		"title" : "Cилові масляні трансформатори з класами напруги до 35 кВ та потужністю до 2500 кВА (ТМ, ТМГ, ТМЗ, ТМЖГ)",
		"series": series,
		"inform": inform,
		"page": 'Трансформатори',
	}

	return render(request, "products/transformers.html", context)

def transformers_tm(request):
	trans_tm = TransformTm.objects.all()
	inform = InformTransform.objects.first()
	context = {
		"title": 'ТМ та ТМЖ',
		"trans_tm": trans_tm,
		"inform": inform,
	}

	return render(request, "products/tm.html", context)





