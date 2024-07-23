import os
import requests
import scrapy
from ..items import AmazontutorialItem


class AmazonspiderSpider(scrapy.Spider):
    # Spider name
    name = 'amazonspider'
    # The URL that we are going to Scrap
    start_urls = ['https://www.amazon.com/s?k=shoes&i=stripbooks-intl-ship&crid=2P0OWBNGX1ZSB&sprefix=shoes%2Cstripbooks-intl-ship%2C385&ref=nb_sb_noss_1']

    def parse(self, response):
        # Items is an instance from the class AmazonTutorialItem
        items = AmazontutorialItem()
        # Product's Name
        name = response.css('.a-color-base.a-text-normal::text').extract()
        # Product's Author
        brand = response.css('.a-color-secondary .a-size-base+ .a-size-base').css('::text').extract()
        # Product's Price
        price = response.css('.a-price-whole').css('::text').extract()
        # Product's Image
        images = response.css('.s-image::attr(src)').extract()

        items['name'] = name
        items['brand'] = brand
        items['price'] = price
        items['image'] = images

        download_images(images, 'C:/Users/aliga/OneDrive/Desktop/Amazon Scraper Images')
        # Yield is used to return from a function without destroying the states of its local variable
        yield items


def download_images(images, folder):
    i = 0
    os.chdir(os.path.join(os.getcwd(), folder))
    for image in images:
        link = image
        with open("pic" + str(i) + ".jpg", "wb") as f:
            im = requests.get(link)
            f.write(im.content)
        i += 1
