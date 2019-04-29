# -*- coding: utf-8 -*-
import scrapy
from datetime import datetime
from pirahna.items import PirahnaItem


class IndoorSpider(scrapy.Spider):
    name = 'indoor'
    allowed_domains = ['piranha.cl']
    start_urls = ['https://www.piranha.cl/kit-base/68/kit-tesla-60-t180w-completo.html']

    def parse(self, response):
        # extraccion del precio
        precio_desc_str = response.css('#our_price_display::text').extract()[0].strip()
        precio_orig_str = response.css('#old_price_display::text').extract()[0].strip()

        precio_descuento = self.parse_str(precio_desc_str)
        precio_original = self.parse_str(precio_orig_str)

        #print(precio_descuento)
        #print(precio_original)

        objeto_precio = PirahnaItem()
        objeto_precio['fecha_crawl'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        objeto_precio['perc_descuento'] = 1 - (precio_descuento/precio_original)
        objeto_precio['precio_original'] = precio_original
        objeto_precio['precio_descuento'] = precio_descuento
        objeto_precio['url'] = response.request.url

        yield objeto_precio


    def parse_str(self, request_str):
        # eliminacion del signo peso, los espacios en blanco y la coma
        request_str = (request_str.replace('$', '').strip()).replace(',', '')

        # transformacion a integer y return
        return int(request_str)
