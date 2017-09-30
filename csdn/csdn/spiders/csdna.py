# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from Csdn.items import CsdnItem
from scrapy.selector import Selector


class CsdnaSpider(CrawlSpider):
    name = 'csdna'
    allowed_domains = ['blog.csdn.net']
    start_urls = ['http://blog.csdn.net/peihaozhu/article/list/1',]

    rules = (
        Rule(LinkExtractor(allow=r'/peihaozhu/article/list/\d+'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        # i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        # return i
        sel = response.selector
        posts = sel.xpath('//')
