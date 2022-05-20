# WaybackShot
WaybackShot provides a simple to use API that allows users to retrieve Screenshots of webpages stored on the Wayback Machine.


## Installation (coming soon)
```bash
pip3 install wayback-shot
```

## How to use it
A basic example of how to use WaybackShot is the following:
```python
from waybackshot import WaybackShot
wayback_shot = WaybackShot()

wayback_shot.screenshot("https://www.example.com/")
```
This will save the most recent archived version of the website `https://www.example.com/` in the current folder.

For more flexibility, the following parameters can be passed to the `screenshot` method:
- `url:` URL to request screenshot for.
- `date: (optional)` Date to request screenshot for in format YYYYMMDD. If not specified, the most recent screenshot will be returned.
- `dir: (optional)` Path to save screenshot to. If not specified, the screenshot will be saved to the current working directory.
- `width: (optional)` Width of the screenshot. If not specified, the default width of 1920 will be used.
- `overwrite: (optional)` If True, the screenshot will be overwritten if it already exists. If False, the screenshot will not be overwritten.
        
 
## Development
If you wish to contribute to this package, be sure to follow the steps provied.

### Prerequisites
Before you can start, you have to install all packages used in this package.
```bash
pip3 install -r requirements.txt
```
This will install the following packages:
- requests
- selenium
- webdriver_manager

Furthermore, Python Version 3.9 is needed.
