# -*- coding: utf-8 -*-
from zemun.items import ZemunItem
import scrapy


class ZemunItem(scrapy.Spider):
    name = "galenika"

    start_urls = ['http://digitalnasrbija.org']

    custom_settings = {
       'FEED_URI' : 'tmp/milan.csv'
   }

    def parse(self, response):
        for elem in response.xpath("//img"):
            img_url = elem.xpath("@src").extract_first()
            yield {'image_urls': [img_url]}
