import requests
import urllib
from bs4 import BeautifulSoup
comp_url = "http://www.moneycontrol.com/india/stockpricequote/mining-minerals/20microns/2M"
def stock_price(comp_url):
    url = comp_url
    htmlfile = requests.get(url)
    htmltext = htmlfile.text
    soup = BeautifulSoup(htmltext,'html.parser')
    structured_soup = soup.prettify()
    return soup.find('div',attrs = {"class":"FL PR5 rD_30"}).find('strong').string


