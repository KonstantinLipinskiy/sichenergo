from django.shortcuts import render
from .models import NewsItem

def news(request):
	news_items = NewsItem.objects.all()
	print(news_items)
	context = {
		"title": "Новини",
		'news_items': news_items,
		}

	return render(request, "news/news.html", context)
