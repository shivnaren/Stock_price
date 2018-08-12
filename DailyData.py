from multiprocessing import Pool
import csv
from IntraDayDataRequest import *
import time
import datetime
import sys

def daily_log(comp,filename):
    try:

        if comp['Trade'] == 'Both Trading':
            both_trade_page_source = request(comp['mcurl'])
            both_trade_page_soup = soup_page_source(both_trade_page_source)
            both_trade_content = both_trade_page_soup.find_all('div', {'id': 'content_bse'})
            comp['Open'], comp['Close'], comp['Low'], comp['High'], comp['Previous Close'] = b_intraday(fn_content_soup(both_trade_content))
        elif comp['Trade'] == 'Bse Trading':
            b_page_source = request(comp['mcurl'])
            b_page_soup = soup_page_source(b_page_source)
            b_content = b_page_soup.find_all('div', {'id': 'content_bse'})
            comp['Open'], comp['Close'], comp['Low'], comp['High'], comp['Previous Close'] = b_intraday(fn_content_soup(b_content))
        elif comp['Trade'] == 'Nse Trading':
            n_page_source = request(comp['mcurl'])
            n_page_soup = soup_page_source(n_page_source)
            n_content = n_page_soup.find_all('div', {'id': 'content_nse'})
            comp['Open'], comp['Close'], comp['Low'], comp['High'], comp['Previous Close'] = n_intraday(fn_content_soup(n_content))
        del comp['mcurl'] , comp['Trade']
        with open(filename, 'ab') as outfile:
            fieldnames = ['N_code', 'B_code', 'Name', 'Open', 'Close', 'Low', 'High', 'Previous Close']
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            # writer.writeheader()
            writer.writerow(comp)

    except Exception as ex:
        print [comp['mcurl'], ex]


def pool_handler():
    data = []

    with open('D:\StockRequestData\IntraDayList.csv') as csvfile:
        readcsv = csv.reader(csvfile, delimiter=',')
        for row in readcsv:
            temp = dict()
            # temp['ExcelID'] = row[1]
            temp['N_code'] = row[1]
            temp['B_code'] = row[2]
            temp['Name'] = row[3]
            temp['mcurl'] = row[4]
            # temp['sector'] = row[6]
            temp['Trade'] = row[6]
            data.append(temp)
    date = datetime.date.today()
    path = 'D:\\DailyStockData\\'
    filename = path + str(date) + '_Stockdata.csv'
    with open(filename, 'w') as outfile:
        fieldnames = ['N_code', 'B_code', 'Name', 'Open', 'Close', 'Low', 'High', 'Previous Close']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()

    pool = Pool(8)
    for comp,i in zip(data, range(len(data))):
        if i==0:
            continue
        pool.apply_async(daily_log, args=(comp,filename))
    pool.close()
    pool.join()


if __name__ == '__main__':

    start_time = time.time()
    pool_handler()
    print("--- %s seconds ---" % (time.time() - start_time))


