import urllib.request,json
from .models import Sources,Articles

#Getting api key
api_key = None
#Get base url
base_url = None
#Get article url
article_url = None
#all articles url
all_articles =None

def configure_request(app):
  global api_key,base_url,article_url,all_articles
  api_key =app.config['NEWS_API_KEY']
  base_url =app.config['NEWS_API_BASE_URL']
  article_url =app.config['ARTICLES_API_BASE']
  all_articles =app.config['ALL_ARTICLES_API']

def get_sources(category):
  
  get_sources_url =  base_url.format(category,api_key)  
  
  with urllib.request.urlopen(get_sources_url) as url:
    get_sources_data = url.read()
    get_sources_response = json.loads(get_sources_data)
    
    sources_results = None
    
    if get_sources_response ['sources']:
      sources_results_list = get_sources_response['sources']
      sources_results = process_results(sources_results_list)
      
      
  return sources_results  
