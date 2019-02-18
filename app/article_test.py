import unittest
from models import article
article = article.article

class articleTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the article class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article= Article("urlToImage","description","publishedAt")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))


if __name__ == '__main__':
    unittest.main()