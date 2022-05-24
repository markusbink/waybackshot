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
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


class Helper:
    def create_dir(self, dir: str) -> None:
        """
        Creates the directory specified by the given path if it does not already exist.

        :param dir: Path of directory to create.
        """

        if dir and not os.path.isdir(dir):
            os.mkdir(dir)

    def get_filename_from(self, url: str, date: str, include_date: bool) -> str:
        """
        Returns the filename of the screenshot.

        :param url: URL to get filename of.
        :return: Filename of screenshot.
        """

        filename = url.replace("/", "")
        filename = filename.replace(":", "")

        if include_date:
            filename = f"{date}_{filename}"

        return f"{filename}.png"

    def perform_click(self, driver: webdriver.Chrome, x: int, y: int) -> None:
        """
        Perform a click on the given coordinates.

        :param driver: Selenium driver.
        """

        actions = ActionChains(driver)
        actions.move_by_offset(x, y)
        actions.click()
        actions.perform()


Helper = Helper()
