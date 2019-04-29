# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PirahnaItem(scrapy.Item):
    # define the fields for your item here like:
    fecha_crawl = scrapy.Field()
    precio_descuento = scrapy.Field()
    precio_original = scrapy.Field()
    perc_descuento = scrapy.Field()
    url = scrapy.Field()
