class Article:
    """
    Article class to define article's objects
    """
    def __init__(self,title,name,url,urlToImage,publishedAt,description=None,author=None):
        self.title = title
        self.name = name
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.author = author