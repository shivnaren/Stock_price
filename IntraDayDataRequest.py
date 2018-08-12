from __future__ import print_function
import requests as re
from bs4 import BeautifulSoup
from requests import Response
from requests.adapters import HTTPAdapter
import logging
import datetime




headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/53.0.2785.143 Safari/537.36 '
}

html_file = ''


def request(url):
    global html_file
    s = re.Session()
    s.mount('http://', HTTPAdapter(max_retries=5))
    s.mount('https://', HTTPAdapter(max_retries=5))
    try:
        html_file = s.get(url, headers=headers, timeout=5)  # type: Response

    except Exception as ex:
        print (ex, url)
        # logger.error(ex)
    finally:
        return html_file


def soup_page_source(page_source):
    page_source = page_source.content
    soup = BeautifulSoup(page_source, 'lxml'#'html.parser'
                         )
    return soup


def fn_content_soup(page_source):
    b_str_soup = BeautifulSoup(str(page_source), 'lxml'#'html.parser'
                               )
    return b_str_soup


def b_intraday(fn_str_soup):
    # type: (object) -> object
    def b_open(str_soup):
        open_p = str_soup.find_all('div', {'id': 'b_open'})[0].text
        return open_p

    p_b_open = b_open(fn_str_soup)

    def b_closeorlive(str_soup):
        closeorlive_p = str_soup.find_all('span', {'id': 'Bse_Prc_tick'})[0].text
        return closeorlive_p

    p_b_closerlive = b_closeorlive(fn_str_soup)

    def b_low(str_soup):
        low_p = str_soup.find_all('span', {'id': 'b_low_sh'})[0].text
        return low_p

    p_b_low = b_low(fn_str_soup)

    def b_high(str_soup):
        high_p = str_soup.find_all('span', {'id': 'b_high_sh'})[0].text
        return high_p

    p_b_high = b_high(fn_str_soup)

    def b_previous_close(str_soup):
        previous_close_p = str_soup.find_all('div', {'id': 'b_prevclose'})[0].text
        return previous_close_p

    p_b_previousclose = b_previous_close(fn_str_soup)

    return p_b_open, p_b_closerlive, p_b_low, p_b_high, p_b_previousclose


def n_intraday(fn_str_soup):
    # type: (object) -> object
    def n_open(str_soup):
        open_p = str_soup.find_all('div', {'id': 'n_open'})[0].text
        return open_p

    p_n_open = n_open(fn_str_soup)

    def n_closeorlive(str_soup):
        closeorlive_p = str_soup.find_all('span', {'id': 'Nse_Prc_tick'})[0].text
        return closeorlive_p

    p_n_closrlive = n_closeorlive(fn_str_soup)

    def n_low(str_soup):
        low_p = str_soup.find_all('span', {'id': 'n_low_sh'})[0].text
        return low_p

    p_n_low = n_low(fn_str_soup)

    def n_high(str_soup):
        high_p = str_soup.find_all('span', {'id': 'n_high_sh'})[0].text
        return high_p

    p_n_high = n_high(fn_str_soup)

    def n_previous_close(str_soup):
        previous_close_p = str_soup.find_all('div', {'id': 'n_prevclose'})[0].text
        return previous_close_p

    p_n_previousclose = n_previous_close(fn_str_soup)

    return p_n_open, p_n_closrlive, p_n_low, p_n_high, p_n_previousclose

#
# source_page = request('https://www.moneycontrol.com/india/stockpricequote/computers-software/8kmilessoftwareservices/PMS01')
# page_soup = soup_page_source(source_page)
#
#
# b_div = page_soup.find_all('div', {'id': 'content_bse'})
# n_div = page_soup.find_all('div', {'id': 'content_nse'})
# b_v_open, b_v_close, b_v_low, b_v_high, b_v_pc = b_intraday(fn_content_soup(b_div))
# n_v_open, n_v_close, n_v_low, n_v_high, n_v_pc = n_intraday(fn_content_soup(n_div))
#
# print(b_v_open, b_v_close, b_v_low, b_v_high, b_v_pc)
# print(n_v_open, n_v_close, n_v_low, n_v_high, n_v_pc)
