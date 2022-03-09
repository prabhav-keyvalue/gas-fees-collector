import ast
from scrapers.BaseScraper import BaseScraper
import os

class MyCryptoScraper(BaseScraper):
    MYCRYPTO_URL = 'MYCRYPTO_URL'
    name = 'MYCRYPTO'

    def __init__(self):
        url = os.environ.get(self.MYCRYPTO_URL)
        super().__init__(url, self.name)
    
    def map_gas_fees(self, html):
        price_info = ast.literal_eval(html.text)
        return {
            'low_price': float(price_info['safeLow']),
            'average_price': float(price_info['standard']),
            'high_price': float(price_info['fast'])
        }