from django.shortcuts import render
from .models import Presentation, DocumentsItem, DocumentsInform, ReviewsInfo, ReviewsItem


def company(request):
	return render(request)


def about(request):
	present = Presentation.objects.first()
	context = {
		"title": 'Про нас',
		"present": present,
	}

	return render(request, 'company/about.html', context)


def documents(request):
	items = DocumentsItem.objects.all()
	inform = DocumentsInform.objects.first()
	context = {
		"title": 'Документи',
		"inform": inform,
		"items": items,
	}

	return render(request, 'company/documents.html', context)


def reviews(request):
	items = ReviewsItem.objects.all()
	inform = ReviewsInfo.objects.first()
	context = {
		"title": 'Відгуки',
		"items": items,
		"inform": inform,
	}

	return render(request, 'company/reviews.html', context)