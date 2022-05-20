import os
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


class Helper:
    def create_dir(self, dir: str) -> None:
        """
        Creates the directory specified by the given path if it does not already exist.

        :param dir: Path of directory to create.
        """

        if not os.path.isdir(dir):
            os.mkdir(dir)

    def get_filename_from(self, url: str) -> str:
        """
        Returns the filename of the screenshot.

        :param url: URL to get filename of.
        :return: Filename of screenshot.
        """

        filename = url.replace("/", "")
        filename = filename.replace(":", "")
        return f"{filename}.png"

    def perform_click(self, driver: webdriver.Chrome, x: int, y: int) -> None:
        """
        Perform a click on the given coordinates.

        :param driver: Selenium driver.
        """

        actions = ActionChains(driver)
        # Move to X Button
        actions.move_by_offset(x, y)
        actions.click()
        actions.perform()


Helper = Helper()
