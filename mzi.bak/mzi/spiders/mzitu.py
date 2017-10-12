# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request


class MzituSpider(scrapy.Spider):
    name = 'mzitu'
    allowed_domains = ['mzitu.com']
    start_urls = ['http://www.mzitu.com/all']

    def parse_item(self, response):
        # i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        # i['description'] = response.xpath('//div[@id="description"]').extract()
        # print 'hi hi hi :' + response.text
        # return i
        pass



        return items



