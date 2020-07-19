from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
import re


def simple_get(url):
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None.
    """
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None


def is_good_response(resp):
    """
    Returns True if the response seems to be HTML, False otherwise.
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200 
            and content_type is not None 
            and content_type.find('html') > -1)


def log_error(e):
    """
    It is always a good idea to log errors. 
    This function just prints them, but you can
    make it do anything.
    """
    print(e)

def scrapNews(url,website):
    raw_html = simple_get(url)
    html = BeautifulSoup(raw_html, 'html.parser')
    switcher = {
        'BBC':getBBCArticle,
        'TOI':getTOIArticle,
        'Hindu':getHinduArticle
    }
    func=switcher.get(website,lambda :'Invalid')
    return func(html)
        

def getBBCArticle(html):
    articleTag = html.find('div',class_ = 'story-body__inner')
    result = ''
    for ptag in articleTag.findAll('p'):
            result += ptag.text
    return (result)

def getHinduArticle(html):
    articleTag = html.find('div',id = re.compile('content-body-.*'))
    result = ''
    for tag in articleTag.children:
        if tag.name is not None :
            if'atd-ad' not in tag.get('class',[]) :
                x = re.search('^Also read.*', tag.get_text())
                if not x:
                    result += (tag.get_text())
    return (result)

def getTOIArticle(html):
    articleTag = html.find('div',class_ = '_1_Akb')
    result = ''
    for tag in articleTag.children:
        if tag is not None and tag.string is not None: 
            result += (tag.string)
    return (result)
    
#Scraping BBC.com 
print(scrapNews('https://www.bbc.com/news/world-europe-53455142','BBC'))
 
#Scraping timesofindia.com 
print(scrapNews('https://timesofindia.indiatimes.com/india/govts-cowardly-actions-will-further-embolden-china-rahul-gandhi-on-lac-row/articleshow/77039309.cms','TOI'))

#Scraping timesofindia.com 
print(scrapNews('https://timesofindia.indiatimes.com/world/middle-east/iran-estimates-it-has-25-million-coronavirus-infections/articleshow/77036293.cms','TOI'))

#Scraping thehindu.com 
print(scrapNews('http://www.thehindu.com/news/national/tamil-nadu/analysis-for-tamil-nadus-ruling-aiadmk-sasikala-factor-refuses-to-fade-away/article32121015.ece?homepage=true',
'Hindu'))