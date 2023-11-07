from django.shortcuts import render
from django.http import HttpResponse
from .models import News

# Create your views here.
def homepage(request):
    all_news = News.objects.all()
    context = {'all_news': all_news}
    return render(request, 'News/index.html', context)