import urllib
import requests
from bs4 import BeautifulSoup
#comp_url = "http://www.moneycontrol.com/india/stockpricequote/finance-investments/20thcenturyfinancecorporation/20C"
def Stock_Trading_Check(comp_url):
    url = comp_url
    htmlfile = requests.get(url)
    htmltext = htmlfile.text
    soup = BeautifulSoup(htmltext,'html.parser')
    #structured_soup = soup.prettify()
    if soup.find('div',attrs = {"class":"bseNot"}) =="":
         Company_Trading_exist = soup.find('div',attrs = {"class":"bseNot"})
    else:
        Existince_Check = soup.find('div',attrs = {"class":"bseNot"}).text
    return Existince_Check
