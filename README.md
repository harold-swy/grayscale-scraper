# grayscale-scraper
A scraping tool for Grayscale.co




<h2><u><b>Introduction</b></u></h2>

This is a tool I made for Hyblock Capital to scrape AUM data from Grayscale, the largest digital assets management firm with more than $13B AUM as of Jan 2021.
Grayscale does not provide an API for its users, so scraping is necessary to obtain AUM data.




<h2><u><b>How it works</b></u></h2>

Grayscale uses Cloudflare's Bot Management which makes it difficult for bots to scrape data from their site. I used VeNoMouS's Cloudscraper module to bypass Cloudflare's Bot Management. The program parses the HTML response and generates a CSV file with the following data: Asset Name, AUM ($), Shares Outstanding, <Asset> per share, holdings per share ($), and Market Price Per Share. This program was developed in and is fully working as of January 2021. 
  
Future users may be required to update the scraping methods due to several reasons such as but not limited to: 1) Cloudflare deploying new defenses against scraping, 2) Cloudscraper Module is no longer updated / available (Selenium is a potential alternative scraping method), 3) Grayscale changing HTML/CSS elements on their website.




<h2><u><b>Potential Uses</b></u></h2>

- Grayscale trading indicators (e.g. Market Per Share premium over Holdings Per Share is traditionally viewed as a bulish event as it shows us institutional investors are willing to pay a premium for the assets, believing that price growth will offset the premiums.)

- Grayscale AUM charts (e.g. If Grayscale AUM has been falling for a period of time, it may be viewed as a bearish event as institutional investors are selling their assets for the long term while few investors are entering with fresh buys to offset the selling)




<h2><u><b>Requirements</b></u></h2>

- Python 3.8< 

- Cloudscraper (https://pypi.org/project/cloudscraper/)

- BeautifulSoup (https://pypi.org/project/beautifulsoup4/)

- CSV (https://pypi.org/project/python-csv/)




<h2><u><b>Screenshots</b></u></h2>

![Image of scraper](https://github.com/harold-swy/grayscale-scraper/blob/main/Screenshot.png)
