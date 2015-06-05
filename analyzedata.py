from dbconnect import *
from datetime import datetime
import calendar


class AnalyzeData():
    @staticmethod
    def __printHeader():
        headerStr = "{0:>5} {1:>20} {2:>8} {3:>8} {4:>8} {5:>8} {6:>8} {7:>8} {8:>8} {9:>10} {10:>10} {11:>10} {12:>10} {13:>10} {14:>10}".format(
            'SC_CODE', 'SC_NAME', 'SC_GROUP', 'SC_TYPE', 'OPEN', 'HIGH', 'LOW', 'CLOSE', 'LAST', 'PREVCLOSE',
            'NO_TRADES', 'NO_OF_SHRS', 'NET_TURNOV', 'TDCLOINDI', 'Date')
        print headerStr

    @staticmethod
    def __formatData(dataList):
        dataStr = "{0:20} {1:>8} {2:>8} {3:>8} {4:>8} {5:>8} {6:>8} {7:>8} {8:>8} {9:>10} {10:>10} {11:>10} {12:>10} {13:>10} {14:>10}" \
            .format(*dataList)
        # .format(dataList)
        return dataStr

    @staticmethod
    def __formatDataWithPercentage(dataList):
        dataStr = "{0:20} {1:>8} {2:>8} {3:>8} {4:>8} {5:>8} {6:>8} {7:>8} {8:>8} {9:>10} {10:>10} {11:>10} {12:>10} {13:>10} {14:>10} {15:>10}" \
            .format(*dataList)
        return dataStr

    @staticmethod
    def __printHeaderWithPercentage():
        headerStr = "{0:>5} {1:>20} {2:>8} {3:>8} {4:>8} {5:>8} {6:>8} {7:>8} {8:>8} {9:>10} {10:>10} {11:>10} {12:>10} {13:>10} {14:>10} {15:>10}".format(
            'SC_CODE', 'SC_NAME', 'SC_GROUP', 'SC_TYPE', 'OPEN', 'HIGH', 'LOW', 'CLOSE', 'LAST', 'PREVCLOSE',
            'NO_TRADES', 'NO_OF_SHRS', 'NET_TURNOV', 'TDCLOINDI', 'Date', 'Percentage')
        print headerStr

    @staticmethod
    def __printHeaderTransMoney():
        headerStr = "{0:>5} {1:>20} {2:>8} {3:>8} {4:>8} {5:>8} {6:>8} {7:>8} {8:>8} {9:>10} {10:>10} {11:>10} {12:>10} {13:>10} {14:>10} {15:>10}".format(
            'SC_CODE', 'SC_NAME', 'SC_GROUP', 'SC_TYPE', 'OPEN', 'HIGH', 'LOW', 'CLOSE', 'LAST', 'PREVCLOSE',
            'NO_TRADES', 'NO_OF_SHRS', 'NET_TURNOV', 'TDCLOINDI', 'Date', 'Trans Money')
        print headerStr

    @staticmethod
    def __formatDataTransMoney(dataList):
        dataStr = "{0:20} {1:>8} {2:>8} {3:>8} {4:>8} {5:>8} {6:>8} {7:>8} {8:>8} {9:>10} {10:>10} {11:>10} {12:>10} {13:>10} {14:>10} {15:>10}" \
            .format(*dataList)
        # .format(dataList)
        return dataStr

    @staticmethod
    def __formatDataWithPercentageTransMoney(dataList):
        dataStr = "{0:20} {1:>8} {2:>8} {3:>8} {4:>8} {5:>8} {6:>8} {7:>8} {8:>8} {9:>10} {10:>10} {11:>10} {12:>10} {13:>10} {14:>10} {15:>10} {16:>10}" \
            .format(*dataList)
        return dataStr

    @staticmethod
    def __printHeaderWithPercentageTransMoney():
        headerStr = "{0:>5} {1:>20} {2:>8} {3:>8} {4:>8} {5:>8} {6:>8} {7:>8} {8:>8} {9:>10} {10:>10} {11:>10} {12:>10} {13:>10} {14:>10} {15:>10} {16:>10}".format(
            'SC_CODE', 'SC_NAME', 'SC_GROUP', 'SC_TYPE', 'OPEN', 'HIGH', 'LOW', 'CLOSE', 'LAST', 'PREVCLOSE',
            'NO_TRADES', 'NO_OF_SHRS', 'NET_TURNOV', 'TDCLOINDI', 'Date', 'Percentage', 'Trans Money')
        print headerStr

    @staticmethod
    def getData(startDate, endDate):
        # query = "SELECT * from stock where date BETWEEN strftime('%d-%m-%Y', date(?)) and strftime('%d-%m-%Y', date(?)) order by no_trades desc LIMIT 10"
        query = "SELECT * from stock where date >= ? and date <= ? order by no_trades desc LIMIT 10"
        parameters = [startDate.strftime('%Y%m%d'), endDate.strftime('%Y%m%d')]
        countQuery = "SELECT count(*) from stock where date >= ? and date <= ? order by no_trades desc LIMIT 10"
        db = DB()
        # result = db.cursor.execute(query, parameter)
        if AnalyzeData.__doShowResult(countQuery, parameters) == True:
            AnalyzeData.__printHeader()
            for row in db.cursor.execute(query, parameters):
                print AnalyzeData.__formatData(row)
        else:
            print "No data found for that particular period."


    @staticmethod
    def getDataForDay(date):
        db = DB()
        query = "select * from stock where date = ? order by NO_TRADES DESC LIMIT 10"
        countQuery = "select count(*) from stock where date = ? order by NO_TRADES DESC LIMIT 10"
        parameters = [date.strftime('%Y%m%d')]
        # result = db.cursor.execute(query, parameters)
        if AnalyzeData.__doShowResult(countQuery, parameters) == True:
            AnalyzeData.__printHeader()
            for row in db.cursor.execute(query, parameters):
                print AnalyzeData.__formatData(row)
        else:
            print "No data found for that particular period."

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
    def getDataUsingPercentage(startDate, endDate):
        # query = "SELECT * from stock where date >= ? and date <= ? order by no_trades desc LIMIT 10"
        query = "SELECT *, CAST(no_trades AS DOUBLE) / cast(no_of_shrs as DOUBLE) * cast(100 as DOUBLE) as percentage from stock where percentage < 100 and date >= ? and date <= ? order by percentage DESC LIMIT 10"
        countQuery = "SELECT count(*), CAST(no_trades AS DOUBLE) / cast(no_of_shrs as DOUBLE) * cast(100 as DOUBLE) as percentage from stock where percentage < 100 and date >= ? and date <= ? order by percentage DESC LIMIT 10"
        parameters = [startDate.strftime('%Y%m%d'), endDate.strftime('%Y%m%d')]
        db = DB()
        # result = db.cursor.execute(query, parameters)
        if AnalyzeData.__doShowResult(countQuery, parameters) == True:
            AnalyzeData.__printHeaderWithPercentage()
            for row in db.cursor.execute(query, parameters):
                print AnalyzeData.__formatDataWithPercentage(row)
        else:
            print "No data found for the particular period."

    @staticmethod
    def getDataForDayUsingPercentage(date):
        db = DB()
        # query = "select * from stock where date = ? order by NO_TRADES DESC LIMIT 10"
        query = "SELECT *, CAST(no_trades AS DOUBLE) / cast(no_of_shrs as DOUBLE) * cast(100 as DOUBLE) as percentage from stock where percentage < 100 and date = ? order by percentage DESC LIMIT 10"
        countQuery = "SELECT count(*), CAST(no_trades AS DOUBLE) / cast(no_of_shrs as DOUBLE) * cast(100 as DOUBLE) as percentage from stock where percentage < 100 and date = ? order by percentage DESC LIMIT 10"
        # result = db.cursor.execute(query, [date.strftime('%Y%m%d')])
        parameters = [date.strftime('%Y%m%d')]

        if AnalyzeData.__doShowResult(countQuery, parameters) == True:
            AnalyzeData.__printHeaderWithPercentage()
            for row in db.cursor.execute(query, parameters):
                print AnalyzeData.__formatDataWithPercentage(row)
        else:
            print "No data found for that particular time period."


    @staticmethod
    def getDataForWeekUsingPercentage(startDate, endDate):
        AnalyzeData.getDataUsingPercentage(startDate, endDate)


    @staticmethod
    def getDataForMonthUsingPercentage(month, year):
        startDate = datetime(year, month, 1)
        lastDay = calendar.monthrange(year, month)[1]
        endDate = datetime(year, month, lastDay)
        AnalyzeData.getDataUsingPercentage(startDate, endDate)

    @staticmethod
    def getDataForYearUsingPercentage(year):
        startDate = datetime(year, 1, 1)
        lastDay = calendar.monthrange(year, 12)[1]
        endDate = datetime(year, 12, lastDay)
        AnalyzeData.getDataUsingPercentage(startDate, endDate)

    @staticmethod
    def __doShowResult(query, parameters):
        db = DB()
        result = db.cursor.execute(query, parameters).fetchone()
        count = result[0]
        if int(count) > 0:
            return True
        else:
            return False


    @staticmethod
    def getDataDesc(startDate, endDate):
        # query = "SELECT * from stock where date BETWEEN strftime('%d-%m-%Y', date(?)) and strftime('%d-%m-%Y', date(?)) order by no_trades desc LIMIT 10"
        query = "SELECT * from stock where date >= ? and date <= ? order by no_trades LIMIT 10"
        parameters = [startDate.strftime('%Y%m%d'), endDate.strftime('%Y%m%d')]
        countQuery = "SELECT count(*) from stock where date >= ? and date <= ? order by no_trades LIMIT 10"
        db = DB()
        # result = db.cursor.execute(query, parameter)
        if AnalyzeData.__doShowResult(countQuery, parameters) == True:
            AnalyzeData.__printHeader()
            for row in db.cursor.execute(query, parameters):
                print AnalyzeData.__formatData(row)
        else:
            print "No data found for that particular period."

    @staticmethod
    def getDataForDayDesc(date):
        db = DB()
        query = "select * from stock where date = ? order by NO_TRADES LIMIT 10"
        countQuery = "select count(*) from stock where date = ? order by NO_TRADES LIMIT 10"
        parameters = [date.strftime('%Y%m%d')]
        # result = db.cursor.execute(query, parameters)
        if AnalyzeData.__doShowResult(countQuery, parameters) == True:
            AnalyzeData.__printHeader()
            for row in db.cursor.execute(query, parameters):
                print AnalyzeData.__formatData(row)
        else:
            print "No data found for that particular period."


    @staticmethod
    def getDataForWeekDesc(startDate, endDate):
        AnalyzeData.getDataDesc(startDate, endDate)


    @staticmethod
    def getDataForMonthDesc(month, year):
        startDate = datetime(year, month, 1)
        lastDay = calendar.monthrange(year, month)[1]
        endDate = datetime(year, month, lastDay)
        AnalyzeData.getDataDesc(startDate, endDate)

    @staticmethod
    def getDataForYearDesc(year):
        startDate = datetime(year, 1, 1)
        lastDay = calendar.monthrange(year, 12)[1]
        endDate = datetime(year, 12, lastDay)
        AnalyzeData.getDataDesc(startDate, endDate)

    @staticmethod
    def getDataUsingPercentageDesc(startDate, endDate):
        # query = "SELECT * from stock where date >= ? and date <= ? order by no_trades desc LIMIT 10"
        query = "SELECT *, CAST(no_trades AS DOUBLE) / cast(no_of_shrs as DOUBLE) * cast(100 as DOUBLE) as percentage from stock where percentage < 100 and date >= ? and date <= ? order by percentage LIMIT 10"
        countQuery = "SELECT count(*), CAST(no_trades AS DOUBLE) / cast(no_of_shrs as DOUBLE) * cast(100 as DOUBLE) as percentage from stock where percentage < 100 and date >= ? and date <= ? order by percentage LIMIT 10"
        parameters = [startDate.strftime('%Y%m%d'), endDate.strftime('%Y%m%d')]
        db = DB()
        # result = db.cursor.execute(query, parameters)
        if AnalyzeData.__doShowResult(countQuery, parameters) == True:
            AnalyzeData.__printHeaderWithPercentage()
            for row in db.cursor.execute(query, parameters):
                print AnalyzeData.__formatDataWithPercentage(row)
        else:
            print "No data found for the particular period."

    @staticmethod
    def getDataForDayUsingPercentageDesc(date):
        db = DB()
        # query = "select * from stock where date = ? order by NO_TRADES DESC LIMIT 10"
        query = "SELECT *, CAST(no_trades AS DOUBLE) / cast(no_of_shrs as DOUBLE) * cast(100 as DOUBLE) as percentage from stock where percentage < 100 and date = ? order by percentage LIMIT 10"
        countQuery = "SELECT count(*), CAST(no_trades AS DOUBLE) / cast(no_of_shrs as DOUBLE) * cast(100 as DOUBLE) as percentage from stock where percentage < 100 and date = ? order by percentage LIMIT 10"
        # result = db.cursor.execute(query, [date.strftime('%Y%m%d')])
        parameters = [date.strftime('%Y%m%d')]

        if AnalyzeData.__doShowResult(countQuery, parameters) == True:
            AnalyzeData.__printHeaderWithPercentage()
            for row in db.cursor.execute(query, parameters):
                print AnalyzeData.__formatDataWithPercentage(row)
        else:
            print "No data found for that particular time period."

    @staticmethod
    def getDataForWeekUsingPercentageDesc(startDate, endDate):
        AnalyzeData.getDataUsingPercentageDesc(startDate, endDate)


    @staticmethod
    def getDataForMonthUsingPercentageDesc(month, year):
        startDate = datetime(year, month, 1)
        lastDay = calendar.monthrange(year, month)[1]
        endDate = datetime(year, month, lastDay)
        AnalyzeData.getDataUsingPercentageDesc(startDate, endDate)

    @staticmethod
    def getDataForYearUsingPercentageDesc(year):
        startDate = datetime(year, 1, 1)
        lastDay = calendar.monthrange(year, 12)[1]
        endDate = datetime(year, 12, lastDay)
        AnalyzeData.getDataUsingPercentageDesc(startDate, endDate)

    @staticmethod
    def getDataTransMoney(startDate, endDate):
        # query = "SELECT * from stock where date BETWEEN strftime('%d-%m-%Y', date(?)) and strftime('%d-%m-%Y', date(?)) order by no_trades desc LIMIT 10"
        query = "SELECT *, last * no_of_shrs as totalmoney from stock where date >= ? and date <= ? order by totalmoney desc LIMIT 10"
        parameters = [startDate.strftime('%Y%m%d'), endDate.strftime('%Y%m%d')]
        countQuery = "SELECT count(*), last * no_of_shrs as totalmoney from stock where date >= ? and date <= ? order by totalmoney desc LIMIT 10"
        db = DB()
        # result = db.cursor.execute(query, parameter)
        if AnalyzeData.__doShowResult(countQuery, parameters) == True:
            AnalyzeData.__printHeaderTransMoney()
            for row in db.cursor.execute(query, parameters):
                print AnalyzeData.__formatDataTransMoney(row)
        else:
            print "No data found for that particular period."


    @staticmethod
    def getDataForDayTransMoney(date):
        db = DB()
        query = "select *,last * no_of_shrs as totalmoney from stock where date = ? order by totalmoney DESC LIMIT 10"
        countQuery = "select count(*),last * no_of_shrs as totalmoney from stock where date = ? order by totalmoney DESC LIMIT 10"
        parameters = [date.strftime('%Y%m%d')]
        # result = db.cursor.execute(query, parameters)
        if AnalyzeData.__doShowResult(countQuery, parameters) == True:
            AnalyzeData.__printHeaderTransMoney()
            for row in db.cursor.execute(query, parameters):
                print AnalyzeData.__formatDataTransMoney(row)
        else:
            print "No data found for that particular period."

    @staticmethod
    def getDataForWeekTransMoney(startDate, endDate):
        AnalyzeData.getDataTransMoney(startDate, endDate)


    @staticmethod
    def getDataForMonthTransMoney(month, year):
        startDate = datetime(year, month, 1)
        lastDay = calendar.monthrange(year, month)[1]
        endDate = datetime(year, month, lastDay)
        AnalyzeData.getDataTransMoney(startDate, endDate)

    @staticmethod
    def getDataForYearTransMoney(year):
        startDate = datetime(year, 1, 1)
        lastDay = calendar.monthrange(year, 12)[1]
        endDate = datetime(year, 12, lastDay)
        AnalyzeData.getDataTransMoney(startDate, endDate)


    @staticmethod
    def getDataUsingPercentageTransMoney(startDate, endDate):
        # query = "SELECT * from stock where date >= ? and date <= ? order by no_trades desc LIMIT 10"
        query = "SELECT *, CAST(no_trades AS DOUBLE) / cast(no_of_shrs as DOUBLE) * cast(100 as DOUBLE) as percentage, last * no_of_shrs as totalmoney from stock where percentage < 100 and date >= ? and date <= ? order by percentage DESC LIMIT 10"
        countQuery = "SELECT count(*), CAST(no_trades AS DOUBLE) / cast(no_of_shrs as DOUBLE) * cast(100 as DOUBLE) as percentage, last * no_of_shrs as totalmoney from stock where percentage < 100 and date >= ? and date <= ? order by percentage DESC LIMIT 10"
        parameters = [startDate.strftime('%Y%m%d'), endDate.strftime('%Y%m%d')]
        db = DB()
        # result = db.cursor.execute(query, parameters)
        if AnalyzeData.__doShowResult(countQuery, parameters) == True:
            AnalyzeData.__printHeaderWithPercentageTransMoney()
            for row in db.cursor.execute(query, parameters):
                print AnalyzeData.__formatDataWithPercentageTransMoney(row)
        else:
            print "No data found for the particular period."

    @staticmethod
    def getDataForDayUsingPercentageTransMoney(date):
        db = DB()
        # query = "select * from stock where date = ? order by NO_TRADES DESC LIMIT 10"
        query = "SELECT *, CAST(no_trades AS DOUBLE) / cast(no_of_shrs as DOUBLE) * cast(100 as DOUBLE) as percentage, last * no_of_shrs as totalmoney from stock where percentage < 100 and date = ? order by percentage, totalmoney DESC LIMIT 10"
        countQuery = "SELECT count(*),CAST(no_trades AS DOUBLE) / cast(no_of_shrs as DOUBLE) * cast(100 as DOUBLE) as percentage, last * no_of_shrs as totalmoney from stock where percentage < 100 and date = ? order by percentage, totalmoney DESC LIMIT 10"
        # result = db.cursor.execute(query, [date.strftime('%Y%m%d')])
        parameters = [date.strftime('%Y%m%d')]

        if AnalyzeData.__doShowResult(countQuery, parameters) == True:
            AnalyzeData.__printHeaderWithPercentageTransMoney()
            for row in db.cursor.execute(query, parameters):
                print AnalyzeData.__formatDataWithPercentageTransMoney(row)
        else:
            print "No data found for that particular time period."


    @staticmethod
    def getDataForWeekUsingPercentageTransMoney(startDate, endDate):
        AnalyzeData.getDataUsingPercentageTransMoney(startDate, endDate)


    @staticmethod
    def getDataForMonthUsingPercentageTransMoney(month, year):
        startDate = datetime(year, month, 1)
        lastDay = calendar.monthrange(year, month)[1]
        endDate = datetime(year, month, lastDay)
        AnalyzeData.getDataUsingPercentageTransMoney(startDate, endDate)

    @staticmethod
    def getDataForYearUsingPercentageTransMoney(year):
        startDate = datetime(year, 1, 1)
        lastDay = calendar.monthrange(year, 12)[1]
        endDate = datetime(year, 12, lastDay)
        AnalyzeData.getDataUsingPercentageTransMoney(startDate, endDate)



    @staticmethod
    def getDataDescTransMoney(startDate, endDate):
        # query = "SELECT * from stock where date BETWEEN strftime('%d-%m-%Y', date(?)) and strftime('%d-%m-%Y', date(?)) order by no_trades desc LIMIT 10"
        query = "SELECT *, last * no_of_shrs as totalmoney from stock where date >= ? and date <= ? order by no_trades,totalmoney LIMIT 10"
        parameters = [startDate.strftime('%Y%m%d'), endDate.strftime('%Y%m%d')]
        countQuery = "SELECT count(*), last * no_of_shrs as totalmoney from stock where date >= ? and date <= ? order by no_trades, totalmoney LIMIT 10"
        db = DB()
        # result = db.cursor.execute(query, parameter)
        if AnalyzeData.__doShowResult(countQuery, parameters) == True:
            AnalyzeData.__printHeader()
            for row in db.cursor.execute(query, parameters):
                print AnalyzeData.__formatData(row)
        else:
            print "No data found for that particular period."

    @staticmethod
    def getDataForDayDescTransMoney(date):
        db = DB()
        query = "select *,last * no_of_shrs as totalmoney from stock where date = ? order by NO_TRADES, totalmoney LIMIT 10"
        countQuery = "select count(*), last * no_of_shrs as totalmoney from stock where date = ? order by NO_TRADES, totalmoney LIMIT 10"
        parameters = [date.strftime('%Y%m%d')]
        # result = db.cursor.execute(query, parameters)
        if AnalyzeData.__doShowResult(countQuery, parameters) == True:
            AnalyzeData.__printHeaderTransMoney()
            for row in db.cursor.execute(query, parameters):
                print AnalyzeData.__formatDataTransMoney(row)
        else:
            print "No data found for that particular period."


    @staticmethod
    def getDataForWeekDescTransMoney(startDate, endDate):
        AnalyzeData.getDataDescTransMoney(startDate, endDate)


    @staticmethod
    def getDataForMonthDescTransMoney(month, year):
        startDate = datetime(year, month, 1)
        lastDay = calendar.monthrange(year, month)[1]
        endDate = datetime(year, month, lastDay)
        AnalyzeData.getDataDescTransMoney(startDate, endDate)

    @staticmethod
    def getDataForYearDescTransMoney(year):
        startDate = datetime(year, 1, 1)
        lastDay = calendar.monthrange(year, 12)[1]
        endDate = datetime(year, 12, lastDay)
        AnalyzeData.getDataDescTransMoney(startDate, endDate)

    @staticmethod
    def getDataUsingPercentageDescTransMoney(startDate, endDate):
        # query = "SELECT * from stock where date >= ? and date <= ? order by no_trades desc LIMIT 10"
        query = "SELECT *,last * no_of_shrs as totalmoney, CAST(no_trades AS DOUBLE) / cast(no_of_shrs as DOUBLE) * cast(100 as DOUBLE) as percentage from stock where percentage < 100 and date >= ? and date <= ? order by percentage, totalmoney LIMIT 10"
        countQuery = "SELECT count(*), last * no_of_shrs as totalmoney, CAST(no_trades AS DOUBLE) / cast(no_of_shrs as DOUBLE) * cast(100 as DOUBLE) as percentage from stock where percentage < 100 and date >= ? and date <= ? order by percentage, totalmoney LIMIT 10"
        parameters = [startDate.strftime('%Y%m%d'), endDate.strftime('%Y%m%d')]
        db = DB()
        # result = db.cursor.execute(query, parameters)
        if AnalyzeData.__doShowResult(countQuery, parameters) == True:
            AnalyzeData.__printHeaderWithPercentageTransMoney()
            for row in db.cursor.execute(query, parameters):
                print AnalyzeData.__formatDataWithPercentageTransMoney(row)
        else:
            print "No data found for the particular period."

    @staticmethod
    def getDataForDayUsingPercentageDescTransMoney(date):
        db = DB()
        # query = "select * from stock where date = ? order by NO_TRADES DESC LIMIT 10"
        query = "SELECT *,last * no_of_shrs as totalmoney, CAST(no_trades AS DOUBLE) / cast(no_of_shrs as DOUBLE) * cast(100 as DOUBLE) as percentage from stock where percentage < 100 and date = ? order by percentage,totalmoney LIMIT 10"
        countQuery = "SELECT count(*),last * no_of_shrs as totalmoney, CAST(no_trades AS DOUBLE) / cast(no_of_shrs as DOUBLE) * cast(100 as DOUBLE) as percentage from stock where percentage < 100 and date = ? order by percentage,totalmoney LIMIT 10"
        # result = db.cursor.execute(query, [date.strftime('%Y%m%d')])
        parameters = [date.strftime('%Y%m%d')]

        if AnalyzeData.__doShowResult(countQuery, parameters) == True:
            AnalyzeData.__printHeaderWithPercentageTransMoney()
            for row in db.cursor.execute(query, parameters):
                print AnalyzeData.__formatDataWithPercentageTransMoney(row)
        else:
            print "No data found for that particular time period."

    @staticmethod
    def getDataForWeekUsingPercentageDescTransMoney(startDate, endDate):
        AnalyzeData.getDataUsingPercentageDescTransMoney(startDate, endDate)


    @staticmethod
    def getDataForMonthUsingPercentageDescTransMoney(month, year):
        startDate = datetime(year, month, 1)
        lastDay = calendar.monthrange(year, month)[1]
        endDate = datetime(year, month, lastDay)
        AnalyzeData.getDataUsingPercentageDescTransMoney(startDate, endDate)

    @staticmethod
    def getDataForYearUsingPercentageDescTransMoney(year):
        startDate = datetime(year, 1, 1)
        lastDay = calendar.monthrange(year, 12)[1]
        endDate = datetime(year, 12, lastDay)
        AnalyzeData.getDataUsingPercentageDescTransMoney(startDate, endDate)