import os
import requests
from .helpers import Helper
from os import path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
from typing import Optional


class WaybackShot:
    def __init__(self):
        self.BASE_URL = "https://archive.org/wayback/available"

    def screenshot(
        self,
        url: str,
        date: str = None,
        dir: str = "",
        width: int = 1920,
        overwrite: bool = False,
    ) -> bool():
        """
        Takes a screenshot of the given URL and saves it to the specified location.

        :param url: URL to request screenshot for.
        :param date: (optional) Date to request screenshot for in format YYYYMMDD. If not specified, the most recent screenshot will be returned.
        :param dir: (optional) Path to save screenshot to. If not specified, the screenshot will be saved to the current working directory.
        :param width: (optional) Width of the screenshot. If not specified, the default width of 1920 will be used.
        :param overwrite: (optional) If True, the screenshot will be overwritten if it already exists. If False, the screenshot will not be overwritten if it already exists.
        :return: True if screenshot was found, False if not.
        """
        self.url_to_screenshot = url
        self.dir = dir
        self.width = width

        path_of_image = path.join(
            self.dir, Helper.get_filename_from(self.url_to_screenshot)
        )

        screenshot_exists = path.exists(path_of_image)
        if screenshot_exists and not overwrite:
            print(f"Screenshot for {self.url_to_screenshot} already exists.")
            return

        snapshot_url = self.__getSnapshotURL(self.url_to_screenshot, date)
        if snapshot_url is None:
            return

        self.__getScreenshotFrom(snapshot_url)

    def __getSnapshotURL(self, url: str, date: str = None) -> Optional[str]:
        """
        Returns the URL of the snapshot for the given URL and date.

        :param url: URL to request screenshot for.
        :param date: (optional) Date to request screenshot for in format YYYYMMDD. If not specified, the most recent screenshot will be returned.
        :return: The URL of the snapshot if it exists, otherwise None.
        """

        params = {"url": url, "timestamp": date}

        try:
            response = requests.get(self.BASE_URL, params=params)
            json_response = response.json()

            if (
                not json_response["archived_snapshots"]
                or not json_response["archived_snapshots"]["closest"]["available"]
            ):
                raise Exception(f"No snapshot found for URL {url}.")

            return json_response["archived_snapshots"]["closest"]["url"]

        except Exception as e:
            print(f"Error: {e}")

    def __getScreenshotFrom(self, url: str) -> None:
        """
        Takes a screenshot of the given URL and saves it to the specified location.

        :param url: URL to take screenshot of.
        """
        Helper.create_dir(self.dir)

        driver = self.__get_driver(url)

        # Close Wayback Header
        Helper.perform_click(driver, self.width - 20, 20)

        # Take Screenshot of specified website
        driver.find_element(By.TAG_NAME, "body").screenshot(
            path.join(self.dir, Helper.get_filename_from(self.url_to_screenshot))
        )

        driver.quit()

    def __get_driver(self, url: str) -> webdriver.Chrome:
        """
        Returns a Selenium Chrome driver with the given URL.

        :param url: URL to load in the driver.
        :return: Selenium Chrome driver.
        """

        # Disable logs of webdriver manager
        os.environ["WDM_LOG_LEVEL"] = "0"

        # Create options for driver
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument("--remote-debugging-port=9222") 

        # Init driver
        driver = webdriver.Chrome(
            options=options,
            service=Service(
                ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()
            ),
        )

        # Configure driver
        driver.get(url)
        height = self.__get_window_height(driver)
        driver.set_window_size(self.width, height)

        return driver

    def __get_window_height(self, driver: webdriver.Chrome) -> int:
        return driver.execute_script("return document.body.scrollHeight")


if __name__ == "__main__":
    urls = [
        "https://www.prevention.com/health/a20461629/highly-effective-treatments-for-lower-back-pain/",
        "https://www.fitnessmagazine.com/health/injury/back/back-pain-causes-and-treatments/",
        "https://www.bupa.co.uk/health-information/back-care/back-pain",
        "https://www.mayoclinic.org/",
        "https://en.wikipedia.org/wiki/Mayo_Clinic",
        "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3056276/",
        "https://www.healthline.com/health/lower-back-pain-treatment-options",
        "https://melioguide.com/physical-therapy-continuing-education/traction-back-pain-treatment/",
        "http://seattlebackpain.com/treatment-method-pros-cons/",
        "https://www.cosmeticdentistrycenter.com/blog/can-sealants-eliminate-tooth-decay",
        "https://www.cdc.gov/vitalsigns/dental-sealants/index.html",
        "https://www.mouthhealthy.org/en/az-topics/s/sealants",
        "https://www.cochrane.org/CD001830/ORAL_sealants-preventing-tooth-decay-permanent-teeth",
    ]

    wb = WaybackShot()

    for url in urls:
        wb.screenshot(
            url,
            "20180701",
            "testing",
            1920,
            True,
        )
