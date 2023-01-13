import json
import pickle
import sqlite3


connection = sqlite3.connect("testing.db")
cursor = connection.cursor()

class DatabaseInteractions:
    @staticmethod
    def setup():


