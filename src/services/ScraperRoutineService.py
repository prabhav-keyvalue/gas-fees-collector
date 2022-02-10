
import os

from services.BaseRoutineService import BaseRoutineService
from services.GasService import GasService
from services.SlackService import SlackService

class ScraperRoutineService(BaseRoutineService):

    SCRAPER_INTERVAL = "SCRAPER_INTERVAL"

    def __init__(self):
        super().__init__(ScraperRoutineService.__name__,int(os.environ.get(self.SCRAPER_INTERVAL)))
        self._slack_channel = os.environ.get('SLACK_CHANNEL')
        self._scrapers = os.environ.get('SCRAPERS').split(',')
        self._time_intervals =list(map(int, os.environ.get('GAS_FEES_TRACKING_INTERVALS_IN_HRS').split(',')))
        self.gas_service = GasService()
        self.slack_service = SlackService()

    

    def task(self):
        self.gas_service.fetch_and_save_gas_fees()
        for time_interval in self._time_intervals:
            res = self.gas_service.get_latest_gas_fees(self._scrapers, time_interval)
            slack_message = self.gas_service.build_slack_message(res, time_interval)
            self.slack_service.send_message(slack_message, self._slack_channel)
        self.gas_service.delete_old_rows(max(self._time_intervals))