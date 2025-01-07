import sqlite3

class SQLHandler:
    def __init__(self, conn : sqlite3.Connection, commit : bool =True):
        self.conn = conn
        self.commit = commit

    def write(self, query : str, data : tuple = ()):
        cursor = self.conn.cursor()
        cursor.execute(query, data)

        if self.commit:
            self.conn.commit()

    def writemany(self, query : str, data : list[tuple] = []):
        cursor = self.conn.cursor()
        cursor.executemany(query, data)

        if self.commit:
            self.conn.commit()

    def read(self, query : str, params : tuple):
        cursor = self.conn.cursor()
        cursor.execute(query, params)

        return cursor.fetchall()
