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