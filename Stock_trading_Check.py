import urllib
import requests
from bs4 import BeautifulSoup

print "starting"

#comp_url = "http://www.moneycontrol.com/india/stockpricequote/finance-investments/20thcenturyfinancecorporation/20C"
#comp_url = "http://www.moneycontrol.com/india/stockpricequote/plastics/axelpolymers/AP24\n"
#comp_url = "http://www.moneycontrol.com/india/stockpricequote/chemicals/aartiindustries/AI45"
#comp_url = "http://www.moneycontrol.com/india/stockpricequote/textilesspinningcottonblended/aptyarns/APT01"
#comp_url = "http://www.moneycontrol.com/india/stockpricequote/financeleasinghirepurchase/akscredits/AKS"
def Stock_Trading_Check(comp_url):
    print "in function"
    url = comp_url
    s = requests.Session()
    s.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'
    #r = s.get(url)
    htmlfile = s.get(url)#, allow_redirects=False
    htmltext = htmlfile.text
    soup = BeautifulSoup(htmltext,'html.parser')
    #structured_soup = soup.prettify()
    return soup.find_all('div',attrs = {"class":"bseNot"})
#data = Stock_Trading_Check(comp_url)
#print data
"""i=0
raw_comp_links_list = []
#this is url to find out all prices
def comp_links(alpha_url_para):
    htmlfile = urllib.urlopen(alpha_url_para)
    htmltext = htmlfile.read()
    soup = BeautifulSoup(htmltext,'html.parser')
    table = soup.find('table','pcq_tbl MT10')
    for link_table in table.find_all('tr')[1:]:
        for link_data in link_table.find_all('a'):
            raw_comp_links_list.append(link_data['href'])


alphasymobls = [u'A', u'B', u'C', u'D', u'E', u'F', u'G', u'H', u'I', u'J', u'K', u'L', u'M', u'N', u'O', u'P', u'Q', u'R', u'S', u'T', u'U', u'V', u'W', u'X', u'Y', u'Z', u'others']
while i< len(alphasymobls):
    alpha_url = "http://www.moneycontrol.com/india/stockpricequote/"+alphasymobls[i]
    comp_links(alpha_url)
    i = i + 1

#Removing empty links
All_comp_links_list = [x for x in raw_comp_links_list if x != ""]


print All_comp_links_list
print len(All_comp_links_list
)

"""
trading_in_BSE_NSE_file = open('trading_in_BSE_NSE.txt', 'a')
Not_trading_in_BSE_NSE_file = open('Not_trading_in_BSE_NSE.txt', 'a')
trading_in_one_file = open('trading_in_one.txt', 'a')


trading_in_BSE_NSE = []
trading_in_one = []
Not_trading_in_BSE_NSE = []
print "file open"
k =0
fp = open("links.txt","r")
for line in enumerate(fp):
    print "in file"
    k = k+1
    print k
    if line[1] != "" and line[1] != 0:
        line = line[1].strip('\n')
        data = Stock_Trading_Check(line)

        if len(data) == 2:
            print "NOT_BSE_NSE"
            Not_trading_in_BSE_NSE_file.write("%s\n" % line)
            Not_trading_in_BSE_NSE.append(line)
        elif len(data) == 1:
            print "ONly_ONE"
            trading_in_one_file.write("%s\n" % line)
            trading_in_one.append(line)
        else:
            print "BSE_NSE"
            trading_in_BSE_NSE_file.write("%s\n" % line)
            trading_in_BSE_NSE.append(line)


print len(Not_trading_in_BSE_NSE)
print len(trading_in_one)
print len(trading_in_BSE_NSE)

#------------------------------------------------
"""
print "printing the file Not_trading_in_BSE_NSE"
thefile = open('Not_trading_in_BSE_NSE.txt', 'w')
for link in Not_trading_in_BSE_NSE:
    thefile.write("%s\n"%link)
print "printing the file trading_in_one"
thefile = open('trading_in_one.txt', 'w')
for link in trading_in_one:
    thefile.write("%s\n"%link)
print "printing the file trading_in_BSE_NSE"
thefile = open('trading_in_BSE_NSE.txt', 'w')
for link in trading_in_BSE_NSE:
    thefile.write("%s\n" % link)
"""








