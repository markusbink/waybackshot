# WayBackShot
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



import unittest
import glob
from waybackshot import WaybackShot

class TestNotAvailable(unittest.TestCase):
    wayback_shot = WaybackShot()
    url = "https://storage.googleapis.com/quetechce-com/material/Low_Back_Pain_Lumbar_Traction.pdf"

    def test_no_args(self):
        try:
            self.wayback_shot.screenshot(self.url)
        except:
            self.assertTrue()

if __name__ == '__main__':
    unittest.main()