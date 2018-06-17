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


class Source:
    """
    Sources class to define news source Objects
    """
    def __init__(self,name,description,category,url,language,country):
        self.name = name
        self.description = description
        self.category = category
        self.url = url
        self.language = language
        self.country = country