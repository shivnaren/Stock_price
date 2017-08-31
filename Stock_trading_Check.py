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




trading_in_BSE_NSE = []
trading_in_one = []
Not_trading_in_BSE_NSE = []
fp = open("links.txt")
for line in enumerate(fp):
    if line[1] != "" and line[1] != 0:
        data = Stock_Trading_Check(line[1])
        if len(data) == 2:
            Not_trading_in_BSE_NSE.append(line[1])
        elif len(data) == 1:
            trading_in_one.append(line[1])
        else:
            trading_in_BSE_NSE = [line[1]]


print len(Not_trading_in_BSE_NSE)
print len(trading_in_one)
print len(trading_in_BSE_NSE)
