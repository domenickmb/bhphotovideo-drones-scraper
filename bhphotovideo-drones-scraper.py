#/usr/bin/env python3
"""
========================================================================
Author: Domenick Botardo

Program Name: bhphotovideo-drones-scraper.py

Description:
    This webscraper is for demonstration purposes only. It extracts
    product details regarding drones from https://www.bhphotovideo.com

Usage:
    $ python bhphotovideo-drones-scraper.py
========================================================================
"""
import os
import scrapy
from scrapy.crawler import CrawlerProcess

# The filename where to save the data
FILENAME = 'drones.csv'
landing_page = 'https://www.bhphotovideo.com/c/buy/aerial-quadcopters/ci/23396/N/3765401969'

class DronesSpider(scrapy.Spider):
    name = 'drones'
    allowed_domains = ['bhphotovideo.com']
    start_urls = [landing_page]

    custom_settings = {
        'DOWNLOAD_DELAY': 0.5,
        'CONCURRENT_REQUEST_PER_DOMAIN': 32,
        'FEED_FORMAT': FILENAME.split('.')[-1],
        'FEED_URI': FILENAME
    }

    def parse(self, response):
        # Parse and extract details for each item
        for item in response.xpath('//div[@data-selenium="miniProductPage"]'):
            product_name = item.xpath('.//span[@data-selenium="miniProductPageProductName"]/text()').get()
            product_price = item.xpath('.//span[@data-selenium="uppedDecimalPriceFirst"]/text()').get()
            key_feats = item.xpath('.//*[@data-selenium="miniProductPageSellingPointsListItem"]/text()').getall()
            image_link = item.xpath('.//*[@data-selenium="miniProductPageImg"]/@src').get()
            internal_link = item.css('a.link_29FfdQHOeQOWOre_0jF7Re').attrib['href']
            availability = item.xpath('.//div/span[@data-selenium="stockStatus"]/text()').get()

            # We need to join the internal link with the base url
            # to get the complete product link
            product_link = response.urljoin(internal_link)
            yield {
                'Product Name': product_name,
                'Product Price': product_price,
                'Key Features': key_feats,
                'Availability': availability,
                'Image Link': image_link,
                'Product Link': product_link,
            }

        pagination_links = response.xpath('.//ul/li/a[@data-selenium="listingPagingLink"]/@href').getall()
        yield from response.follow_all(pagination_links, callback=self.parse)


if os.path.isfile(FILENAME):
    os.remove(FILENAME)

process = CrawlerProcess()
process.crawl(DronesSpider)
process.start()
