from django.shortcuts import render
from .models import InformTransform, TransformItem, TransformTm, TransformTmg, TransformTmz, TransformYZ, InformKTP

def products(request):
	return render(request)

def transformers(request):
	series = TransformItem.objects.all()
	inform = InformTransform.objects.first()
	context = {
		"title" : "Трансформатори",
		"series": series,
		"inform": inform,
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

def transformers_tmg(request):
	trans_tmg = TransformTmg.objects.all()
	inform = InformTransform.objects.first()
	context = {
		"title": 'ТМГ та ТМЖГ',
		"trans_tmg": trans_tmg,
		"inform": inform,
	}

	return render(request, "products/tmg.html", context)

def transformers_tmz(request):
	trans_tmz = TransformTmz.objects.all()
	inform = InformTransform.objects.first()
	context = {
		"title": 'ТМЗ',
		"trans_tmz": trans_tmz,
		"inform": inform,
	}

	return render(request, "products/tmz.html", context)

def transformers_yz(request):
	trans_yz = TransformYZ.objects.all()
	inform = InformTransform.objects.first()
	context = {
		"title": 'ТМЗ',
		"trans_yz": trans_yz,
		"inform": inform,
	}

	return render(request, "products/tmg-yz.html", context)

def ktp(request):
	ktp = InformKTP.objects.first()
	context = {
		"title": 'КТП',
		"ktp": ktp,
	}

	return render(request, "products/ktp.html", context)





