
from datetime import datetime
from scrapers.EtherScanScraper import EtherScanScraper
from scrapers.MyCryptoScraper import MyCryptoScraper
from services.DbService import DbService


class GasScraperService:

    def __init__(self):
        self.scrapers = [EtherScanScraper(), MyCryptoScraper()]
        self.db_service= DbService()
    

    def get_all_gas_fees(self):
        print(f'Starting scraping of gas fees at {datetime.now()}')
        for scraper in self.scrapers:
            gas_fees = scraper.scrape_gas_fees()
            print(f'saving to db from source {scraper.name} gas_fees_data: {gas_fees}')
            self.db_service.save_gas_fees({**gas_fees, 'source':scraper.name})
        
