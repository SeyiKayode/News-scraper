import requests
import urllib3
from django.shortcuts import render, redirect
from bs4 import BeautifulSoup as BSoup
from .models import Headline
# Create your views here.

urllib3.disable_warnings()


def scrape(request):
    url = "https://www.naijaloaded.com.ng/"
    page = requests.get(url)
    soup = BSoup(page.content, 'html.parser')
    News = soup.find_all('article', {'class': 'col-md-12'})
    for article in News:
        title = article.find('a')['href']
        image = article.find('a')['href']
        url = article.find('a')['href']
        new_headline = Headline()
        new_headline.title = title
        new_headline.url = url
        new_headline.image = image
        new_headline.save()
    return redirect('../')


def news_list(request):
    headlines = Headline.objects.all()[::-1]
    context = {'object_list': headlines}
    return render(request, 'news/home.html', context)






































