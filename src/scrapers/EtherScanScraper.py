import os
from scrapers.BaseScraper import BaseScraper

class EtherScanScraper(BaseScraper):
    ETHERSCAN_URL = 'ETHERSCAN_URL'
    name = 'ETHERSCAN'

    def __init__(self):
        url = os.environ.get(self.ETHERSCAN_URL)
        super().__init__(url, self.name)

    def map_gas_fees(self, html):
        low_price = html.find('#spanLowPrice', first=True).text
        average_price = html.find('#spanAvgPrice', first=True).text
        high_price = html.find('#spanHighPrice', first=True).text
        
        return {
            'low_price':float(low_price),
            'average_price':float(average_price),
            'high_price':float(high_price)
        }
