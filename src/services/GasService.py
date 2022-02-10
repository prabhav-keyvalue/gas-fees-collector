from services.DbService import DbService
from services.GasScraperService import GasScraperService
from prettytable import PrettyTable

class GasService:

    def __init__(self):
        self.gas_scraper_service = GasScraperService()
        self.db_service = DbService()
        
    def build_slack_message(self,result, time_interval):
        t = PrettyTable(['source', 'low price', 'average price', 'high price'])
        t.align = 'l'
        t.padding_width = 5
        t.border = False
        for key in result:
            t.add_row([key, result[key]['low_price'], result[key]['average_price'], result[key]['high_price']])
        
        return f'Gas Fees Report for interval {time_interval}hrs \n{t.get_string()}'

    def fetch_and_save_gas_fees(self):
        self.gas_scraper_service.get_all_gas_fees()

    def get_latest_gas_fees(self,sources, time_interval):
        res = self.db_service.get_latest_gas_fees(sources, time_interval)
        print(f'fecthed lastest gas fees from sources: {sources} for time interval: {time_interval}')
        return res

    def get_all_gas_fees(self):
        return self.db_service.get_all_gas_fees()

    def delete_old_rows(self, time_interval):
        print(f'deleting gas fees enteries older than {time_interval}hrs')
        self.db_service.delete_old_rows(time_interval)