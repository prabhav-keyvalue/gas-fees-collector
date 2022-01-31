from services.DbService import DbService
from services.GasScraperService import GasScraperService


class GasService:

    def __init__(self):
        self.gas_scraper_service = GasScraperService()
        self.db_service = DbService()
        

    def fetch_and_save_gas_fees(self):
        self.gas_scraper_service.get_all_gas_fees()

    def get_latest_gas_fees(self):
        self.db_service.get_latest_gas_fees()

    def get_all_gas_fees(self):
        self.db_service.get_all_gas_fees()