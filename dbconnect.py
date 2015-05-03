import sqlite3


class DB:
    def __init__(self, dbpath='SQLite_DB\\stocks.db'):
        self.conn = sqlite3.connect(dbpath)
        self.cursor = self.conn.cursor()


    def __exit__(self):
        self.conn.close()

    def execute(self, query, parameters=()):
        self.cursor.execute(query, parameters)



# conn = sqlite3.connect('SQLite_DB\stocks')
# c = conn.cursor()
#
# for row in c.execute('SELECT * FROM stock'):
#     print row



