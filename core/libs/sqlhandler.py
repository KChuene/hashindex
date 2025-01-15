import sqlite3
import os

# Prevent from being created when API starts
def singleton(Class):
    instances = {}

    def create(commit : bool = True):
        if not Class in instances:
            instances[Class] = Class(commit)

        return instances[Class]
    
    return create

@singleton
class SQLHandler:
    def __init__(self, commit : bool =True):
        if not os.path.exists("./db"):
            os.mkdir("./db")

        self.dbconn = sqlite3.connect("./db/hindex.db", check_same_thread=False)
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