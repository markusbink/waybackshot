import unittest
import glob
from waybackshot import WaybackShot

class TestNoArgs(unittest.TestCase):
    wayback_shot = WaybackShot()
    url = "https://iwh.on.ca/summaries/research-highlights/is-traction-effective-in-treating-low-back-pain"

    def test_no_args(self):
        self.wayback_shot.screenshot(self.url, dir="screenshots")
        self.assertTrue(len(glob.glob('screenshots/*.png'))>0)

if __name__ == '__main__':
    unittest.main()
