import requests
from datetime import date
import os


NEWS_API_KEY = open('./news_api.txt').read()

def search_topic(query):
    url = ('https://newsapi.org/v2/everything?'
       f'q=T{query}'
       f'from={date.today()}&'
       'sortBy=popularity&'
       f'apiKey={NEWS_API_KEY}')
    return url


def from_tech_crunch():
    url = ('https://newsapi.org/v2/top-headlines?'
        'sources=TechCrunch&'
        f'apiKey={NEWS_API_KEY}')
    return url


def from_news24():
    url = ('https://newsapi.org/v2/everything?'
        'domains=news24.com&'
        f'apiKey={NEWS_API_KEY}')
    return url

# # news from country
def business_new_from_usa():
    url = ('https://newsapi.org/v2/top-headlines?'
        'country=us&category=business&'
        'apiKey=cb91f0bacf2547178828105cd1a47d3a')


def send_request(url):
    response = requests.get(url)
    return response.json()

def filter_response(response):
    f_res = ""

    if response['status'] == "ok":
        for i in range(response['totalResults']):
            f_res += response['articles'][i]['title'] +"\n"
            f_res += response['articles'][i]['description'] +"\n\n"
            # url_to_article = response['articles'][i]['url'] # try use this url to scrap the full article content from the site.
    else:
        f_res = "No news articles found"
    return f_res


if __name__ == "__main__":
    url = from_tech_crunch()
    url = from_news24()
    res = send_request(url)
    f_res = filter_response(res)
    print(f_res)
