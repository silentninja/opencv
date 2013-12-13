from bs4 import BeautifulSoup

from urllib2 import urlopen


url = "https://news.ycombinator.com/"
i=0
html = urlopen(url).read()
soup = BeautifulSoup(html)


for tags in soup.findAll("td", {"class": "title"}):

    if(i>2):
        break
    else:
        b=tags.find("a")
        if b is None:
            continue

        else:
            print(b.get('href'))
            i+=1


