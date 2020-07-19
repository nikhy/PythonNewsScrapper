import NewsScrapper as ns
#Scraping BBC.com 
print(ns.scrapNews('https://www.bbc.com/news/world-europe-53455142','BBC'))
 
#Scraping timesofindia.com 
print(ns.scrapNews('https://timesofindia.indiatimes.com/india/govts-cowardly-actions-will-further-embolden-china-rahul-gandhi-on-lac-row/articleshow/77039309.cms','TOI'))

#Scraping timesofindia.com 
print(ns.scrapNews('https://timesofindia.indiatimes.com/world/middle-east/iran-estimates-it-has-25-million-coronavirus-infections/articleshow/77036293.cms','TOI'))

#Scraping thehindu.com 
print(ns.scrapNews('http://www.thehindu.com/news/national/tamil-nadu/analysis-for-tamil-nadus-ruling-aiadmk-sasikala-factor-refuses-to-fade-away/article32121015.ece?homepage=true',
'Hindu'))