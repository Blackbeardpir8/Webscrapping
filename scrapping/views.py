from django.shortcuts import render
from .script import scrap_imdb_news
from django.http import JsonResponse
from .models import News

# Create your views here.
def run_scraper(request):
    scrap_imdb_news()
    return JsonResponse({
        'status':True,
        'message': 'Scrapper Executed'
    })


def index(request):
    return render(request,'index.html',context={
            "news_data":News.objects.all()
    })