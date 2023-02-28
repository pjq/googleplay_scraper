## Introduction
This script uses the google_play_scraper library to scrape information about an app from the Google Play Store. The library provides several functions to scrape different data, such as app details, reviews and ratings, etc.

The script writes the scraped data to a local file in the following format:

- app_detail_{app_pkg}.txt for the app details
- app_reviews_{app_pkg}.txt for the reviews of the app
- app_reviews_all_{app_pkg}.txt for all the reviews of the app

### implement refer:
- https://pypi.org/project/google-play-scraper/

## Requirements
- google_play_scraper library
- Python 3.x

```bash
pip3 install -r requirements.txt
```
## Usage
```commandline
 python3 googleplay_scraper.py -p "com.google.android.apps.googlevoice" --http_proxy "http://proxy:8080" --https_proxy "https://proxy:8080" 
```


```commandline
usage: googleplay_scraper.py [-h] -p APP_PKG [-x HTTP_PROXY] [-y HTTPS_PROXY]

Google Play Scraper

optional arguments:
  -h, --help            show this help message and exit
  -p APP_PKG, --app_pkg APP_PKG
                        The package name of the app to scrape
  -x HTTP_PROXY, --http_proxy HTTP_PROXY
                        The http proxy
  -y HTTPS_PROXY, --https_proxy HTTPS_PROXY
                        The https proxy
```
