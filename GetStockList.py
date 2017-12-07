# -*- coding: utf-8 -*-
import re
import requests
from bs4 import BeautifulSoup
import os
import pymysql
import logging

def main():
    if not os.path.isdir('log'):
        os.makedirs('log')
    logging.basicConfig(filename='log/getlist-error.log',
                        level=logging.ERROR,
                        format='%(asctime)s\t[%(levelname)s]\t%(message)s',
                        datefmt='%Y/%m/%d %H:%M:%S')

    db = pymysql.connect("localhost", "user", "user1234", "StockCrawler", use_unicode=True, charset="utf8")
    cursor = db.cursor()

    url = "http://isin.twse.com.tw/isin/C_public.jsp?strMode=2"
    res = requests.get(url, verify = False)
    soup = BeautifulSoup(res.text, 'lxml')

    try:
        deleteSql = "DELETE FROM StockList"
        cursor.execute(deleteSql)
        db.commit()

        kind = ""
        for row in soup.select('tr'):
            cols = row.find_all('td')
            data = re.search('(.*)　(.*)', cols[0].text)
            if data is not None:
                if data.group(1) is not None:
                    if data.group(2) is not None:
                        stockId = data.group(1).strip()
                        name = data.group(2).strip()
                        listingDate = cols[2].text.strip()
                        industry = cols[4].text.strip()
                        print(stockId, name, listingDate, industry)

                        try:
                            sql = "INSERT INTO StockList(StockId, \
                                   Name, ListingDate, Industry, Kind) \
                                   VALUES ('%s', '%s', '%s', '%s', '%s')" % \
                                  (stockId, name, listingDate, industry, kind)
                            cursor.execute(sql)
                            db.commit()
                        except Exception as e:
                            print(e)
                            logging.error("insert data error → StockId:" + stockId + ", RowData:" + str(data) + ", error msg:" + str(e))
                            db.rollback()
            else:
                print(cols.__len__())
                if cols.__len__() == 1 :
                    kind = cols[0].text.strip()


    except Exception as e:
        print(e)
        logging.error("delete or get data error → error msg:" + str(e))
    db.close()


if __name__ == '__main__':
    main()

