import urllib
import requests
from bs4 import BeautifulSoup


#comp_url = "http://www.moneycontrol.com/india/stockpricequote/finance-investments/20thcenturyfinancecorporation/20C"
#comp_url = "http://www.moneycontrol.com/india/stockpricequote/plastics/axelpolymers/AP24"
def Stock_Trading_Check(comp_url):
    url = comp_url
    htmlfile = requests.get(url)
    htmltext = htmlfile.text
    soup = BeautifulSoup(htmltext,'html.parser')
    #structured_soup = soup.prettify()
    return soup.find_all('div',attrs = {"class":"bseNot"})
#data = Stock_Trading_Check(comp_url)




trading_list = []
Not_trading_list = []
fp = open("links.txt")
for line in enumerate(fp):
    if line[1] != "" and line[1] != 0:
        data = Stock_Trading_Check(line[1])

    if not data[0] in "is not traded on BSE in the last 30 days" and not data[0] in "is not traded":
        print "starting Not trading list"
        print line
        print data
        
        print "ENDING Not trading list"
        Not_trading_list.append(line)
    else:
        print "starting trading list"
        print line
        print data
        print "ENDING trading list"
        trading_list.append(line)

print len(trading_list)
print len(Not_trading_list)
