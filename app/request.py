from app import app
import urllib.request,json
from .models import news
from .models import article

News = news.News
Article = article.Article


# Getting api key
api_key = app.config['NEWS_API_KEY']
# # Getting thenews base url
base_url = app.config["NEWS_API_BASE_URL"]
base_url_article = app.config["ARTICLE_API_BASE_URL"]


def get_news(category):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_sources = None

        if get_news_response['sources']:
           news_sources_list = get_news_response['sources']
           news_sources = process_sources(news_sources_list)

    return news_sources

def process_sources(news_list):
    '''
    Function  that processes the news result and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain news details

    Returns :
        news_sources: A list of news objects
    '''
    news_sources = []
    for news_item in news_list:
        id = news_item.get('id')
        name = news_item.get('name')
        description = news_item.get('description')
        url = news_item.get('url')
        category = news_item.get('category')
        language = news_item.get('language')
        country = news_item.get('country')

        if id:
            news_object = News(id,name,description,url,category,language,country )
            news_sources.append(news_object)

    return news_sources

    def get_news(id):
        get_news_details_url = base_url.format(id,api_key)

    with urllib.request.urlopen(get_news_details_url) as url:
        news_details_data = url.read()
        news_details_response = json.loads(news_details_data)

        news_object = None
        if news_details_response:
            id = news_details_response.get('id')
            name = news_details_response.get('name')
            description = news_details_response.get('description')
            url = news_details_response.get('url')
            category = news_details_response.get('category')
            language = news_details_response.get('language')
            country = news_details_response.get('country')

            news_object = News(id,name,description,url,category,language,country)

    return news_object

def get_articles(id):
    '''
    Function that gets the json response to our url request
    '''
    get_articles_url = base_url_article.format(id,api_key)

    with urllib.requests.urlopen(get_articles_url) as url:
        get_articles_response = json.loads(url.read())
        article_results = None

        if get_articles_response['articles']:
           article_results_list = get_articles_response['articles']
           article_results = process_results(article_results_list)

    return article_results

def process_results(article_list):
    '''
    Function  that processes the article result and transform them to a list of Objects

    Args:
       article_list: A list of dictionaries that containarticle details

    Returns :
       article_articles: A list of article objects
    '''
    article_results= []
    for article_item in article_list:
       
       title =article_item.get('title')
       urlToimage = article_item.get('urlToimage')
       description = article_item.get(' description ')
       publishedAt = article_item.get(' publishedAt')
       url = article_article_item.get ('url')
      

       if  urlToimage:
           article_object =Article (title,urlToimage,description,publishedAt,url)
           article_results.append(article_object)

    return article_results

    




