import urllib.request
import pprint as p

def getHtml(url):
    html = urllib.request.urlopen(url).read()
    return html


aurl = "http://www.runoob.com/python3/python3-tutorial.html"
html = getHtml(aurl)
print (html)
p.pprint(html.decode())

