import sqlite3
import uuid

from util.Singleton import Singleton

class DbService(metaclass=Singleton):

    def __init__(self):
        self.conn = sqlite3.connect(':memory:')
        self.cursor = self.conn.cursor()
        with self.conn:
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS gas_fees (
                                    id TEXT NOT NULL PRIMARY KEY,
                                    source TEXT NOT NULL,
                                    low_price REAL NOT NULL,
                                    average_price REAL NOT NULL,
                                    high_price REAL NOT NULL,
                                    created_at TEXT NOT NULL
                                    )
                                """)
    
    def save_gas_fees(self, gas_fees_data):
        id = str(uuid.uuid4())
        gas_fees_data =  {**gas_fees_data, 'id': id}
        print(f'Saving gas fees data {gas_fees_data} to db')
        try:
            with self.conn:
                self.cursor.execute("""INSERT INTO gas_fees VALUES (
                                        :id, 
                                        :source, 
                                        :low_price, 
                                        :average_price, 
                                        :high_price,
                                        datetime('now'))""",gas_fees_data)
        except Exception as e:
            print(f'Failed to save gas fees data to db - {gas_fees_data}, Error - {e}') 
    
    def get_latest_gas_fees(self):
        self.cursor.execute("""select * from gas_fees
                                group by source, created_at
                                order by  created_at DESC LIMIT 2""")

        res = self.cursor.fetchall()

        print(f'latest gas fees {res}')

        return res

    def get_all_gas_fees(self):
        self.cursor.execute('select * from gas_fees')
        res = self.cursor.fetchall()
        print(f'all gas fees stored - {res}')

        return res
        