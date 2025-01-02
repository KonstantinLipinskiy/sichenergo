from django.shortcuts import render

from .models import Contacts, ContactsLocation

def contacts(request):
	contact = Contacts.objects.first()
	location = ContactsLocation.objects.first()
	context = {
		"title": 'Контакти',
		"contact": contact,
		"location": location,
	}

	return render(request, 'contacts/contacts.html', context)