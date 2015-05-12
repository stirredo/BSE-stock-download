from dbconnect import *
from datetime import datetime
import calendar


class AnalyzeData():
    @staticmethod
    def getData(startDate, endDate):
        # query = "SELECT * from stock where date BETWEEN strftime('%d-%m-%Y', date(?)) and strftime('%d-%m-%Y', date(?)) order by no_trades desc LIMIT 10"
        query = "SELECT * from stock where date >= ? and date <= ? order by no_trades desc LIMIT 10"
        parameter = [startDate.strftime('%Y%m%d'), endDate.strftime('%Y%m%d')]
        db = DB()
        AnalyzeData.__printHeader()
        for row in db.cursor.execute(query, parameter):
            print AnalyzeData.__formatData(row)


    @staticmethod
    def getDataForDay(date):
        db = DB()
        query = "select * from stock where date = ? order by NO_TRADES DESC LIMIT 10"
        AnalyzeData.__printHeader()
        for row in db.cursor.execute(query, [date.strftime('%Y%m%d')]):
            print AnalyzeData.__formatData(row)

    @staticmethod
    def getDataForWeek(startDate, endDate):
        AnalyzeData.getData(startDate, endDate)


    @staticmethod
    def getDataForMonth(month, year):
        startDate = datetime(year, month, 1)
        lastDay = calendar.monthrange(year, month)[1]
        endDate = datetime(year, month, lastDay)
        AnalyzeData.getData(startDate, endDate)

    @staticmethod
    def getDataForYear(year):
        startDate = datetime(year, 1, 1)
        lastDay = calendar.monthrange(year, 12)[1]
        endDate = datetime(year, 12, lastDay)
        AnalyzeData.getData(startDate, endDate)

    @staticmethod
    def __printHeader():
        headerStr = "{0:>5} {1:>20} {2:>8} {3:>8} {4:>8} {5:>8} {6:>8} {7:>8} {8:>8} {9:>10} {10:>10} {11:>10} {12:>10} {13:>10} {14:>10}".format(
            'SC_CODE', 'SC_NAME', 'SC_GROUP', 'SC_TYPE', 'OPEN', 'HIGH', 'LOW', 'CLOSE', 'LAST', 'PREVCLOSE',
            'NO_TRADES', 'NO_OF_SHRS', 'NET_TURNOV', 'TDCLOINDI', 'Date')
        print headerStr

    @staticmethod
    def __formatData(dataList):
        dataStr = "{0:20} {1:>8} {2:>8} {3:>8} {4:>8} {5:>8} {6:>8} {7:>8} {8:>8} {9:>10} {10:>10} {11:>10} {12:>10} {13:>10} {14:>10}"\
            .format(*dataList)
            #.format(dataList)
        return dataStr

