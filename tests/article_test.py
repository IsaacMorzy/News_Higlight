import unittest
from .app.models import Article

class Article_Test(unittest.TestCase):
    """
    Test class to test the behavior of the Article class
    """
    def setUp(self):
        """
        set up  method will run before every Test
        """
        self.new_article = Article("title","name","description","www.test.com","test.com/img","2018-04-07T12:33:45Z","musyoka")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))
