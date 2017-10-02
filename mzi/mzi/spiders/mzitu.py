# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from mzi.items import MziItem
from scrapy.selector import Selector

class MzituSpider(CrawlSpider):
    name = 'mzitu'
    allowed_domains = ['mzitu.com']
    start_urls = ['http://www.mzitu.com/all']

    rules = (
        # Rule(LinkExtractor(allow=r'/all/\?',restrict_xpaths=('//div[@class="all"]//ul[@class="archives"]')), callback='parse_item', follow=False),
        Rule(LinkExtractor(allow=r'',restrict_xpaths=('//div[@class="all"]//ul[@class="archives"]')), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        # i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        # i['description'] = response.xpath('//div[@id="description"]').extract()
        # print 'hi hi hi :' + response.text
        # return i



        sel = response.selector
        pages = sel.xpath('//*[@class="all"]')
        items = []

        for page in pages:
            item = MziItem()
            item['img_name'] = page.xpath('.//ul[@class="archives"]//p[@class="url"]/a/text()').extract()
            # item['page_url'] = page.xpath('.//ul[@class="archives"]//p[@class="url"]/a/@href').extract()

            items.append(item)
        return items



