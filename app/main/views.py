from flask import render_template,redirect,url_for,request
from . import main
from ..requests import get_headline_articles,get_news_sources,search_language_based,get_headline_search,get_all_source_result
from .forms import LanguageForm
from ..models import Article,Source,News
import json


@main.route('/', methods=['GET', 'POST'])
def index():
    """
	View root page function that returns the index page and its data
	"""
    title = "Coverage You Can Count On"
    form = LanguageForm(request.form)
    show_category = request.args.get('cat')
    hide_keyword = request.args.get('item_h')
    general = get_news_sources('general')
    technology = get_news_sources('technology')
    business = get_news_sources ('business')


    if request.method=='POST' and form.validate():
        language_selected = form.language.data
        return redirect(url_for('.lang',lan=language_selected))
    else:
        return render_template('index.html',title=title,select_box = form ,general=general,technology=technology,business=business)


@main.route('/headlines/<category>')
def headlines(category):
    """
	View headlines page function that returns the headline page and its data
	"""
    title = "headline"
    form = LanguageForm(request.form)
    headlines = get_headline_articles(category)

    return render_template('headline.html',title=title,headline=headlines,select_box = form)



@main.route('/source/<link>')
def source(link):
    """
    View function to display the news of a clicked news source
    """
    link = link.replace(" ","+")
    sources = get_all_source_result(link)
    return render_template('sources.html',sources=sources)

@main.route('/language/<lan>')
def lang(lan):
    '''
    View function to display news based on Language
    '''
    title = f'News in {lan}'
    set_language_results = search_language_based(lan,'sources')
    return render_template('language.html',title=title,source_req=set_language_results)

@main.route('/search', methods=['GET', 'POST'])
def search():
    '''
    View search function that returns search results
    '''
   
    item = request.form.get('item')
    #item = request.args.get('for')
    result = []
    source_list = get_headline_search(item)
    if item:
        result_l = get_headline_articles()
        for res in result_l:
            if item in res.title or res.name or res.description:
                result.append(res)
        #result = search_language_based(item,'headline')
        #result  = get_headline_search(search_one)
    return render_template('result.html',result=result)
