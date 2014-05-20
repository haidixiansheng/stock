from bs4 import BeautifulSoup
import urllib2
import time

# global constants
FILE_NAME = "stock_list"
URL = "http://www.investing.com"

f =  open(FILE_NAME, 'r')

for line in f:
    if line == "":
        break
    pair = line.split("|")
    name = pair[0]
    subUrl = pair[1]

    # daily screen
    urlDaily = URL+subUrl.rstrip()+"-technical?period=86400"
    reqD = urllib2.Request(urlDaily, headers={'User-Agent' : "Magic Browser"})
    contentD = urllib2.urlopen(reqD).read()
    soupD = BeautifulSoup(contentD)

    indicatorD = soupD.find_all("span", {"class" : "greenFont bold"})

    # 5 Hour screen
    urlFiveHour = URL+subUrl.rstrip()+"-technical?period=18000"
    req5H = urllib2.Request(urlFiveHour, headers={'User-Agent' : "Magic Browser"})
    content5H = urllib2.urlopen(req5H).read()
    soup5H = BeautifulSoup(content5H)

    indicator5H = soup5H.find_all("span", {"class" : "greenFont bold"})



    if indicatorD is None:
        print name, "at url", urlDaily, "returns None (Daily)"
    elif indicator5H is None :
        print name, "at url", urlFiveHour, "returns None (Five Hour)"
    elif(len(indicatorD) == 4 and len(indicator5H) == 4) :
        print name, "is a good pick"
  #  else :
 #       print name, "has", len(indicator), "Strong Buy"
    time.sleep(1)


f.close()
