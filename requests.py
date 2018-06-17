from app import app # import the flask application instance
import urllib.request,json #urllib.request module that creates a connection to the API URL and send a request and json modules that will format the JSON response to a Python dictionary.
from .models import Article,Source,News

api_key = None
headlines_url = None
source_url = None
everything_url = None
search_url = None

def configure_request(app): #We access the configuration objects by calling app.config['name_of_object'
    global api_key,headlines_url,everything_url,source_url
    api_key = app.config['NEWS_API_KEY']
    headlines_url = app.config['NEWS_HEADLINES_URL']
    source_url = app.config['NEWS_SOURCE_URL']
    everything_url=app.config['NEWS_EVERYTHING_URL']
    search_url = app.config['NEWS_HEADLINES_URL']


def get_headline_articles(category='general'): 
    #function that takes in an article category
    '''
	Function that gets the json response to our headlines url request
	'''
    get_headline_url = headlines_url.format(category,api_key) 
    #We use the .format() method on the headlines_url and pass in the movie category and the api_key. this will replace the {} curly brace placeholders in the base_url with the category and api_key respectively
     #get_headline_url is the final url of the news api request
    with urllib.request.urlopen(get_headline_url) as url:
        #with (as our context manager)to send a request using the urllib.request.urlopen() function that takes in the get_headlines_url as an argument and sends a request as url
        get_headlines_data = url.read() 
        #reads the response $ store it in the get_headlines_data 
        get_headlines_response = json.loads(get_headlines_data) 
        #convert the JSON response to a Python dictionary using json.loads function and pass in the get_headlines_data variable.



        headlines_results = None

        if get_headlines_response['articles']:
            headlines_result_list=get_headlines_response['articles']
            headlines_results = process_headlines(headlines_result_list) 
            #check if the response contains any results. If it does we call a process_results() function that takes in the list of dictionary objects and returns a list of article objects .

    return headlines_results 
    #Return headline_results which is a list of article objects.


def process_headlines(headlines_list):# function that takes in a list of dictionaries
    '''
    	Function  that processes the headlines result and transform them to a list of Objects

    	Args:
        	headlines_list: A list of dictionaries that contain news headlines

    	Returns :
        	headlines_results: A list of news headlines objects
	'''
    headlines_results = [] #empty list to store the newly created article objects

    for headline in headlines_list or []:#loop through the list of dictionaries using the get() method and pass in the keys so that I can access the respective values.
        title = headline.get('title')
        name = headline.get('source.name')
        description = headline.get('description')
        url = headline.get('url')
        urlToImage = headline.get('urlToImage')
        publishedAt = headline.get('publishedAt')
        author = headline.get('author')

    if urlToImage: #checks if the headline has an image then create the article object
        article_object = Article(title,name,url,urlToImage,publishedAt,description,author)
        headlines_results.append(article_object)

    return headlines_results# returns the list with article objects