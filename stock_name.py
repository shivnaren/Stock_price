import requests
import urllib
from bs4 import BeautifulSoup
comp_url = "http://www.moneycontrol.com/india/stockpricequote/mining-minerals/20microns/2M"
def stock_code(comp_url):
    url = comp_url
    htmlfile = requests.get(url)
    htmltext = htmlfile.text
    soup = BeautifulSoup(htmltext,'html.parser')
    #structured_soup = soup.prettify()
    data = soup.find('div',attrs = {"class":"FL gry10"}).text.encode('utf-8')
    for pipe in range(len(data)):
        decode('utf-8')
stock_code(comp_url)
