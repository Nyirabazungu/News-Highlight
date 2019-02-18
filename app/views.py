from flask import render_template
from app import app
from .request import get_news

# Views

@app.route('/')
def index():

# @app.route('/news/<int:news_id>')
# def news(news_id):

    '''
    View root page function that returns the index page and its data
    '''
# Getting business movie
    business_news = get_news('business')
    print(business_news)
    title = 'Home - Welcome to The best Movie Review Website Online'
    return render_template('index.html', title = title,business = business_news)

 