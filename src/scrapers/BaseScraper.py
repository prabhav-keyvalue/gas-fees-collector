from abc import ABC, abstractmethod
from requests_html import HTMLSession

from services.DbService import DbService

class BaseScraper(ABC):
    
    def __init__(self, url, name):
        self._URL = url
        self._name = name
        self._session = HTMLSession()
    
    def scrape_gas_fees(self):
        try:
            response = self._session.get(self._URL)
            mapped_gas_fees = self.map_gas_fees(response.html)
            return mapped_gas_fees
        except Exception as e:
            print(f'Failed to fetch gas fees from {self._URL}. Error - {e}')
            return None


    @abstractmethod
    def map_gas_fees(self, html):
        pass