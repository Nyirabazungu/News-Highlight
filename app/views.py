from flask import render_template
from app import app
from .request import get_news,get_articles
# from .request import get_article,get_article



# Views

@app.route('/')
def index():

# @app.route('/news/<int:news_id>')
# def news(news_id):

    '''
    View root page function that returns the index page and its data
    '''

    business_news= get_news('business')  
    sports_news = get_news('sports')   
    technology_news = get_news('technology')

    title = 'Home - Welcome to The best News Review Website Online'
    return render_template('index.html', business = business_news ,sports =sports_news, technology= technology_news )


    # bloomberg_article = get_article('bloomberg')  
    # espn_article = get_article('espn')   
    # engadget_article= get_article('engadget')

    # title = 'Home - Welcome to The best Review Website Online'
    # return render_template('index.html',bloomberg = bloomberg_article,espn =espn_article, engadget= engadget_article)

@app.route('/article/<id>')
def article(id):

    '''
    View article page function that returns the article details page and its data
    '''
    articles = get_articles(id)
   
    # title = f'{article.title}'

    return render_template('article.html',articles = articles)


    

    
    

 