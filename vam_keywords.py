import newspaper
from newspaper import Source, ArticleException

import pprint
from newspaper import Article
results = []
with open('visited.txt','rU') as file:
	data = file.readlines()

for url in data:
    a = Article(url, keep_article_html=False)
    try:
        a.download()
        a.parse()
        a.nlp()
        results.append({
    'url': url.encode('utf8'),
    'summary':a.summary.encode('utf8'),
    'keywords':[v.encode('utf8') for v in a.keywords],
    'text':a.text.encode('utf8')
    })
        print a.summary
        print a.keywords
    except :
        pass

pprint.pprint(results)
import csv
toCSV = results
keys = ['url', 'summary', 'keywords','text']
f = open('vamsite.csv', 'wb')
dict_writer = csv.DictWriter(f, keys)
dict_writer.writer.writerow(keys)
dict_writer.writerows(toCSV)    

import json
with open('vamsitedata.txt', 'w') as outfile:
    json.dump(results, outfile)
 