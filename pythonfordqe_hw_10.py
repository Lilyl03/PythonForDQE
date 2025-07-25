# -*- coding: utf-8 -*-
"""PythonForDQE_hw_10.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1i-wQMAQ6pT5goMqWRVMviM-1r3jXxoH1
"""

import sqlite3

class DatabaseSaver:
    def __init__(self, db_path='records.db'):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self._create_tables()

    def _create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS news (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                text TEXT,
                city TEXT,
                timestamp TEXT,
                UNIQUE(text, city, timestamp)
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS private_ad (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                text TEXT,
                expiration_date TEXT,
                timestamp TEXT,
                UNIQUE(text, expiration_date, timestamp)
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS event_announcement (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                text TEXT,
                event_date TEXT,
                location TEXT,
                timestamp TEXT,
                UNIQUE(text, event_date, location, timestamp)
            )
        ''')
        self.conn.commit()

    def save_news(self, record):
        try:
            self.cursor.execute('''
                INSERT INTO news (text, city, timestamp) VALUES (?, ?, ?)
            ''', (record.text, record.city, record._timestamp.strftime('%Y-%m-%d %H:%M:%S')))
            self.conn.commit()
        except sqlite3.IntegrityError:
            print("Duplicate News skipped.")

    def save_private_ad(self, record):
        try:
            self.cursor.execute('''
                INSERT INTO private_ad (text, expiration_date, timestamp) VALUES (?, ?, ?)
            ''', (record.text, record.expiration_date.strftime('%Y-%m-%d'), record._timestamp.strftime('%Y-%m-%d %H:%M:%S')))
            self.conn.commit()
        except sqlite3.IntegrityError:
            print("Duplicate PrivateAd skipped.")

    def save_event_announcement(self, record):
        try:
            self.cursor.execute('''
                INSERT INTO event_announcement (text, event_date, location, timestamp) VALUES (?, ?, ?, ?)
            ''', (record.text, record.event_date.strftime('%Y-%m-%d'), record.location, record._timestamp.strftime('%Y-%m-%d %H:%M:%S')))
            self.conn.commit()
        except sqlite3.IntegrityError:
            print("Duplicate EventAnnouncement skipped.")

    def close(self):
        self.conn.close()

db = DatabaseSaver()

text = "Python 3.12 released with exciting new features."
city = "Yerevan"
output_path = 'output.txt'


record = News(text, city)
record.publish(output_path)
db.save_news(record)