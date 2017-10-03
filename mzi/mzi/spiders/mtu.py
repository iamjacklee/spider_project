# -*- coding: utf-8 -*-
import scrapy
from mzi.items import MziItem
import requests
from scrapy.http import Request


class MtuSpider(scrapy.Spider):
    name = 'mtu'
    allowed_domains = ['mzitu.com']
    start_urls = ['http://mzitu.com/all']

    def parse(self, response):
        
        pages = response.xpath('//*[@class="all"]//ul//li//p[@class="url"]/a')
        # items = []
        item = MziItem()
        for page in pages:                        

            item['fileName'] = page.xpath('./text()').extract()[0]
            item['siteURL'] = page.xpath('./@href').extract()[0]

            # items.append(item)
            # yield item
            # item['siteURL'] = 'http://www.mzitu.com/104369'
            yield Request(url=item['siteURL'],callback=self.parse_one,meta={'item1':item})


    def parse_one(self,response):
        # pass
        item2 = response.meta['item1']
        source = requests.get(response.url)
        html = source.text.encode('utf-8')

        num = response.xpath('//div[@class="pagenavi"]/a/span/text()').extract()[-2]
        items = []

        for i in range(1,int(num)+1):
            item = MziItem()
            item['fileName'] = item2['fileName']
            item['path'] = item['fileName'] + '/'+ str(i) + '.jpg'
            item['pageURL'] = response.url + '/' + str(i)
            items.append(item)

        for item in items:
            yield Request(url=item['pageURL'],meta={'item2':item},callback=self.parse_two)

    def parse_two(self,response):
        # pass
        item = MziItem()
        item3 = response.meta['item2']

        URL = response.xpath('//div[@class="main-image"]//img/@src').extract()[0]
        item['detailURL'] = URL
        item['path'] = item3['path']
        item['fileName'] = item3['fileName']

        yield item



        
