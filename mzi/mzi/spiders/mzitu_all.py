# -*- coding: utf-8 -*-
import scrapy
from mzi.items import MziItem
from scrapy.http import Request

class MzituAllSpider(scrapy.Spider):
    name = 'mzitu_all'
    allowed_domains = ['mzitu.com']
    start_urls = ['http://mzitu.com/all']

    def parse(self, response):
        # pass
        pages = response.xpath('//*[@class="all"]//ul//li//p[@class="url"]/a')
        # pages = response.xpath('//*[@class="all"]//ul//li//p[@class="url"]/a')[:1]
        # pages = ['http://www.mzitu.com/104557']
        items = []
        
        for page in pages:                        
            item = MziItem()
            # item['fileName'] = page.xpath('./text()').extract()[0]
            item['siteURL'] = page.xpath('./@href').extract()[0]
            item['fileName'] = item['siteURL'].split('/')[-1]

            items.append(item)            

        for item in items:
            # yield item
            yield Request(url=item['siteURL'],callback=self.parse_one,meta={'item1':item})

    def parse_one(self,response):
        # pass
        item2 = response.meta['item1']        

        num = response.xpath('//div[@class="pagenavi"]/a/span/text()').extract()[-2]
        pageURL = response.url
        items = []        

        for i in range(1,int(num)+1):
            item = MziItem()
            # item['fileName'] = item2['fileName']
            # item['path'] = response.url.split('/')[-1]
            # item['path'] = item['fileName'] + '/'+ str(i) + '.jpg'
            item['pageURL'] = pageURL + '/' + str(i)
            item['isdown'] = '0'

            # yield item['pageURL']

            
            items.append(item)
           
        for item in items:
            # yield Request(url=item['pageURL'],dont_filter=True,meta={'item2':item},callback=self.parse_two)
            yield item
            
