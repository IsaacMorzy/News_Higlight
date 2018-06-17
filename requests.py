import urllib.request,json
from .models import Article,Source,News

api_key = None
headlines_url = None
source_url = None
everything_url = None
search_url = None

def configure_request(app):
    global api_key,headlines_url,everything_url,source_url
    api_key = app.config['NEWS_API_KEY']
    headlines_url = app.config['NEWS_HEADLINES_URL']
    source_url = app.config['NEWS_SOURCE_URL']
    everything_url=app.config['NEWS_EVERYTHING_URL']
    search_url = app.config['NEWS_HEADLINES_URL']