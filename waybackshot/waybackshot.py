# WaybackShot
# Copyright (C) 2022 Markus Bink and Marcos Fernández-Pichel
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os
import requests
from .helpers import Helper
from os import path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
from typing import Optional, Tuple


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
        include_date: bool = False,
    ) -> None:
        """
        Takes a screenshot of the given URL and saves it to the specified location.

        :param url: URL to request screenshot for.
        :param date: (optional) Date to request screenshot for in format YYYYMMDD. If not specified, the most recent screenshot will be returned.
        :param dir: (optional) Path to save screenshot to. If not specified, the screenshot will be saved to the current working directory.
        :param width: (optional) Width of the screenshot. If not specified, the default width of 1920 will be used.
        :param overwrite: (optional) If True, the screenshot will be overwritten if it already exists. If False, the screenshot will not be overwritten if it already exists.
        :param include_date: (optional) If True, the screenshot will be saved with the date of the snapshot. If False, the screenshot will be saved without the date of the snapshot.
        :return: True if screenshot was found, False if not.
        """
        self.url_to_screenshot = url
        self.dir = dir
        self.width = width
        self.include_date = include_date

        snapshot_url, snapshot_date = self.__getSnapshotInfo(
            self.url_to_screenshot, date
        )

        filename = Helper.get_filename_from(
            self.url_to_screenshot, snapshot_date, self.include_date
        )

        path_of_image = path.join(self.dir, filename)

        screenshot_exists = path.exists(path_of_image)
        if screenshot_exists and not overwrite:
            print(f"Screenshot for {self.url_to_screenshot} already exists.")
            return

        self.date = snapshot_date
        if snapshot_url is None:
            return

        self.__getScreenshotFrom(snapshot_url)

    def __getSnapshotInfo(
        self, url: str, date: str = None
    ) -> Optional[Tuple[str, str]]:
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

            url = json_response["archived_snapshots"]["closest"]["url"]
            timestamp = json_response["archived_snapshots"]["closest"]["timestamp"]

            # Get date from timestamp
            date = timestamp[0:8]

            return url, date

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
        filename = Helper.get_filename_from(
            self.url_to_screenshot, self.date, self.include_date
        )
        driver.find_element(By.TAG_NAME, "body").screenshot(
            path.join(self.dir, filename)
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
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--remote-debugging-port=9222")
        options.add_argument("--force-device-scale-factor=1")

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
        """
        Get the height of the websites body element.

        :param driver: Selenium Chrome driver.
        :return: Height of websites body element.
        """
        return driver.execute_script("return document.body.scrollHeight")


if __name__ == "__main__":
    urls = [
        "https://www.researchgate.net/publication/11353143_Melatonin_in_sleep_disorders_and_jet-lag",
        # "https://www.webmd.com/oral-health/guide/tooth-decay-prevention",
        # "https://www.prevention.com/health/a20461629/highly-effective-tVjreatments-for-lower-back-pain/",
    ]

    wb = WaybackShot()

    for url in urls:
        wb.screenshot(url=url, date="20180701", overwrite=True, include_date=True)
