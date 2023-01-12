import json
import pickle
import sqlite3


class DatabaseInteractions:
    def __init__(self):
        self.connection = sqlite3.connect('currency_history.db')
        self.cursor = self.connection.cursor()

