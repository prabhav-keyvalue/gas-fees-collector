
import os

from services.BaseRoutineService import BaseRoutineService
from services.GasService import GasService

class ScraperRoutineService(BaseRoutineService):

    SCRAPER_INTERVAL = "SCRAPER_INTERVAL"

    def __init__(self):
        interval = os.environ.get(self.SCRAPER_INTERVAL)
        super().__init__(ScraperRoutineService.__name__,int(interval))
        self.gas_service = GasService()
    

    def task(self):
        self.gas_service.fetch_and_save_gas_fees()
        self.gas_service.get_latest_gas_fees()
        self.gas_service.get_all_gas_fees()