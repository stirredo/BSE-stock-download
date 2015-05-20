import os
import requests
import StringIO
import zipfile
import csv
import sys

from dbconnect import DB


class DownloadStock:
    # http://www.bseindia.com/download/BhavCopy/Equity/EQ050115_CSV.ZIP
    urlpattern = 'http://www.bseindia.com/download/BhavCopy/Equity/EQ{0}_CSV.ZIP'

    def __init__(self, date, verbose=False):
        self.verbose = verbose
        self.date = date
        self.fileName = '{0}{1}{2}'.format('EQ', self.date.strftime('%d%m%y'), '.CSV')
        if not self.__checkDateInDatabase():
            if self.__downloadFile():
                if (verbose == True):
                    print "Data for ", date.strftime('%d-%m-%Y'), "successfully downloaded. Parsing file."
                self.__parseFile()
        else:
            if (verbose == True):
                print 'Skipping file: ', self.fileName, ' as its already in database', '\n'


    def __buildUrl(self):
        return self.urlpattern.format(self.date.strftime('%d%m%y'))


    def __downloadFile(self):
        url = self.__buildUrl()

        r = requests.get(url)
        if (r.ok) and (zipfile.is_zipfile(StringIO.StringIO(r.content))):

            z = zipfile.ZipFile(StringIO.StringIO(r.content))
            z.extractall(os.path.join(os.path.curdir, 'zip_files'))
            return True
        else:
            return False

    def __parseFile(self):
        path = '{0}{1}{2}'.format("zip_files","/", self.fileName)
        path = os.path.join(os.path.curdir, 'zip_files', self.fileName)
        with open(path, 'rb') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            data = []
            for row in reader:
                row.append(self.date.strftime('%Y%m%d'))
                # row.append(self.date.strftime('%d-%m-%Y'))
                data.append(row)
            data.pop(0)
            self.__storeStockFile(data)


    def __storeStockFile(self, data):
        db = DB()
        query = "INSERT INTO `stock`(`SC_CODE`,`SC_NAME`,`SC_GROUP`,`SC_TYPE`,`OPEN`,`HIGH`,`LOW`,`CLOSE`,`LAST`,`PREVCLOSE`,`NO_TRADES`,`NO_OF_SHRS`,`NET_TURNOV`,`TDCLOINDI`,`Date`) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
        db.cursor.executemany(query, data)
        db.conn.commit()
        db.conn.close()


    def __checkDateInDatabase(self):
        db = DB()
        query = "SELECT count(*) as count from stock where date=?"
        arguments = [self.date.strftime('%Y%m%d')]

        count = db.cursor.execute(query, arguments)
        count = count.fetchone()[0]
        if count > 0:
            return True
        else:
            return False


    def __getDateInFormat(self, format='%d-%m-%Y'):
        return self.date.strftime(format)


