# WaybackShot

[![PyPI](https://img.shields.io/pypi/v/waybackshot?color=brightgreen)](https://pypi.org/project/waybackshot/)

A simple API to retrieve screenshots of webpages stored on the Wayback Machine.

## Installation

```bash
pip install waybackshot
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
- `filename: (optional)` Filename to save screenshot as. If not specified, the URL will be used.
- `dir: (optional)` Path to save screenshot to. If not specified, the screenshot will be saved to the current working directory.
- `width: (optional)` Width of the screenshot. If not specified, the default width of 1920 will be used.
- `overwrite: (optional)` If True, the screenshot will be overwritten if it already exists, otherwise it will not be overwritten.
- `include_date: (optional)` If True, the screenshot will be saved with the date of the snapshot, otherwise without it.

A full example might look like this:

```python
from waybackshot import WaybackShot
wayback_shot = WaybackShot()

wayback_shot.screenshot(
        url="https://www.example.com/",
        date="20220520",
        filename="example-filename",
        dir="images",
        width=1920,
        overwrite=True,
        include_date=True,
    )
```

This will safe the screenshot of `https://www.example.com/` from the closest match to the given date in a folder named `images` with a width of 1920px. If an image with the same name in the same folder already exists, it wil be overwritten. Further, the filename includes the date of the retrieved snapshot as well as uses the specified filename.

## Development

If you wish to contribute to this package, be sure to follow the steps provied.

### Prerequisites

Before you can start, you have to install all packages used in this package.

```bash
pip install -r requirements.txt
```

This will install the following packages:

- requests
- selenium
- webdriver_manager

Furthermore, Python Version 3.9 is needed.
