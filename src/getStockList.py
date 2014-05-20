from bs4 import BeautifulSoup
import urllib2

# get the stock list
URL = "http://www.investing.com/indices/us-spx-500-components"

fileName = "stock_list"
f = open(fileName, 'w')

req = urllib2.Request(URL, headers={'User-Agent' : "Magic Browser"})
content = urllib2.urlopen(req).read()
soup = BeautifulSoup(content)

allStockTag = soup.find_all("td", {"class" : "bold left noWrap elp"})


for s in allStockTag:
    f.write(s.text + "|" + s.find("a")['href']+"\n")

# close the file handler
f.close()

