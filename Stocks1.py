import urllib
import requests
from bs4 import BeautifulSoup
import re
import os.path
i=0
raw_comp_links_list = []
#this is url to find out all prices
def comp_links(alpha_url_para):
    htmlfile = urllib.urlopen(alpha_url)
    htmltext = htmlfile.read()
    soup = BeautifulSoup(htmltext,'html.parser')
    table = soup.find('table','pcq_tbl MT10')
    for link_table in table.find_all('tr')[1:]:
        for link_data in link_table.find_all('a'):
            raw_comp_links_list.append(link_data['href'])
            print link_data['href']

alphasymobls = [u'A', u'B', u'C', u'D', u'E', u'F', u'G', u'H', u'I', u'J', u'K', u'L', u'M', u'N', u'O', u'P', u'Q', u'R', u'S', u'T', u'U', u'V', u'W', u'X', u'Y', u'Z', u'others']
while i< len(alphasymobls):
    alpha_url = "http://www.moneycontrol.com/india/stockpricequote/"+alphasymobls[i]
    comp_links(alpha_url)
    i = i + 1

print len(raw_comp_links_list)
comp_links_list = [x for x in raw_comp_links_list if x != ""]
print len(comp_links_list)


def stock_price(comp_url):
    url = comp_url
    htmlfile = requests.get(url)
    htmltext = htmlfile.text
    soup = BeautifulSoup(htmltext,'html.parser')
    structured_soup = soup.prettify()
    return soup.find('div',attrs = {"class":"FL PR5 rD_30"}).find('strong').string
stock_price_data = {}
for i in range(len(comp_links_list)):
    price = stock_price(comp_links_list[i])


    print stock_price(comp_url)



