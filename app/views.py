from flask import render_template
from app import app
from .request import get_news,get_news

# Views

@app.route('/')
def index():

# @app.route('/news/<int:news_id>')
# def news(news_id):

    '''
    View root page function that returns the index page and its data
    '''

    business_news = get_news('business')  
    sports_news = get_news('sports')   
    technology_news = get_news('technology')

    title = 'Home - Welcome to The best News Review Website Online'
    return render_template('index.html', business = business_news ,sports =sports_news, technology= technology_news )


    
@app.route('/news/<int:id>')
def news(id):

    '''
    View news page function that returns the news details page and its data
    '''
    news = get_news(id)
    title = f'{news.title}'

    return render_template('news.html',title = title,news = news)

 