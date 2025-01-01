from django.shortcuts import render
from .models import Presentation

def company(request):
	return render(request)

def about(request):
	present = Presentation.objects.first()
	context = {
		"tittle": 'Про нас',
		"present": present,
	}

	return render(request, 'company/about.html', context)