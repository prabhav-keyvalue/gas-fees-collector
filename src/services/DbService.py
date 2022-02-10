from datetime import datetime
import uuid
from util.Singleton import Singleton

class DbService(metaclass=Singleton):

    def __init__(self):
        self._db = []
        self._fields = ['low_price', 'average_price', 'high_price']

    
    def save_gas_fees(self, gas_fees_data):
        _gas_fees_data = {**gas_fees_data, 'id':str(uuid.uuid4()), 'created_at':datetime.now()}
        self._db.append(_gas_fees_data)

    def get_latest_gas_fees(self, sources, time_interval):
        result = {}

        for source in sources:
            result[source] = {}

        now = datetime.now()
        
        for row in self._db:
            source = row['source']
            time_diff = now - row['created_at']

            time_diff_in_hrs = divmod(time_diff.total_seconds(), 3600)[0]

            if time_diff_in_hrs > time_interval:
                continue
            
            for field in self._fields:
                if (field not in result[source]) or (result[source][field] > row[field]):
                    result[source][field]= row[field]
        return result


    def delete_old_rows(self, time_interval):

        new_db = []
        now = datetime.now()

        for row in self._db:
            time_diff = now - row['created_at']

            time_diff_in_hrs = divmod(time_diff.total_seconds(), 3600)[0]

            if time_diff_in_hrs <= time_interval:
                new_db.append(row)

        self._db = new_db



    def get_all_gas_fees(self):
        return self._db