class Article:
    '''
    Article class to define Article Objects
    '''

    def __init__(urlToImage,description,publishedAt):
        self.urlToImage = urlToImage
        self.description= description
        self.publishedAt = publishedAt
        # self.poster = 'https://image.tmdb.org/t/p/w500/'+ poster
        # self.vote_average = vote_average
        # self.vote_count = vote_count