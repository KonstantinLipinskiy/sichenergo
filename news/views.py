from django.shortcuts import render

def news(request):
	context = {
		"title": "Новини", 
		}

	return render(request, "news/news.html", context)
