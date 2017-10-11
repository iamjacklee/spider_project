# -*- coding: utf-8 -*-
import scrapy
from mzi.items import MziItem

class MzituAllSpider(scrapy.Spider):
    name = 'mzitu_all'
    allowed_domains = ['mzitu.com']
    start_urls = ['http://mzitu.com/all']

    def parse(self, response):
        # pass
        pages = response.xpath('//*[@class="all"]//ul//li//p[@class="url"]/a')[:1]
        # pages = ['http://www.mzitu.com/104557']
        items = []
        
        for page in pages:                        
            item = MziItem()
            # item['fileName'] = page.xpath('./text()').extract()[0]
            item['siteURL'] = page.xpath('./@href').extract()[0]
            item['fileName'] = item['siteURL'].split('/')[-1]

            items.append(item)
            # yield item
            # item['siteURL'] = 'http://www.mzitu.com/104369'

        for item in items:
            yield Request(url=item['siteURL'],callback=self.parse_one,meta={'item1':item})
