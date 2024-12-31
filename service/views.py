from django.shortcuts import render
from .models import ServiceInform

def service(request):
	serviceinform = ServiceInform.objects.first()
	context = {
		"title": 'Послуги',
		"serviceinform": serviceinform,
	}

	return render(request, "service/service.html", context)
