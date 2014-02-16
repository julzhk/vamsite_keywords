import newspaper
from newspaper import Source

vam_source = Source('http://www.vam.ac.uk/')

print vam_source.size() # no articles, we have not built the source
vam_source.build()
print vam_source.size()

for article in vam_source.articles:
    print article.url
    print '.'
print ','


from newspaper import Article
a = Article('http://www.vam.ac.uk/content/articles/d/drawing-techniques/', keep_article_html=True)
#a.download()
#a.parse()
#a.nlp()
#print a.summary
#print a.keywords

ignorelist = [
        'vam.ac.uk/whatson','youtube.com','amazon.co.uk','flickr.com',
        'twitter.com','facebook.com','vandashop.com', 'collections.vam']
        if any ([(i in link.url) for i in ignorelist]):
            return
        with open('visited.txt','a') as file:
            file.write('%s\n' % link.url)
        def fail(self, link):
            print 'failed:', repr(link.url)

p = Polly(links=['http://www.vam.ac.uk/'], delay=0.5,domains='vam.ac.uk')
while not p.done:
    p.crawl(method=DEPTH, cached=False, throttle=3)
 