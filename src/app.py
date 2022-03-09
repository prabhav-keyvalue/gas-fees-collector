from dotenv import load_dotenv
from scrapers.EtherScanScraper import EtherScanScraper
from scrapers.MyCryptoScraper import MyCryptoScraper
from services.GasService import GasService
from services.ScraperRoutineService import ScraperRoutineService

load_dotenv()


def main():

    scraper_routine_service = ScraperRoutineService()
    scraper_routine_service.start()

if __name__ == '__main__':
    main()