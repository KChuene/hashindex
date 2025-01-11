import sqlite3

def singleton(Class):
    instances = {}

    def create(*args):
        if not Class in instances:
            instances[Class] = Class(*args)

        return instances[Class]
    
    return create

@singleton
class SQLHandler:
    def __init__(self, conn : sqlite3.Connection, commit : bool =True):
        self.dbconn = conn
        self.commit = commit

    def write(self, query : str, data : tuple = ()):
        cursor = self.dbconn.cursor()
        cursor.execute(query, data)

        if self.commit:
            self.dbconn.commit()

    def writemany(self, query : str, data : list[tuple] = []):
        cursor = self.dbconn.cursor()
        cursor.executemany(query, data)

        if self.commit:
            self.dbconn.commit()

    def read(self, query : str, params : tuple):
        cursor = self.dbconn.cursor()
        cursor.execute(query, params)

        return cursor.fetchall()