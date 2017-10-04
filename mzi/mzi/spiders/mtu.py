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


    def parse_one(self,response):
        # pass
        item2 = response.meta['item1']
        # source = requests.get(response.url)
        # html = source.text.encode('utf-8')

        num = response.xpath('//div[@class="pagenavi"]/a/span/text()').extract()[-2]
        pageURL = response.url
        items = []
        print 'num is :--->' + num
        print 'pageURL:--->' + pageURL
        print 'filename :--->' +item2['fileName']

        for i in range(1,int(num)+1):
            item = MziItem()
            item['fileName'] = item2['fileName']
            # item['path'] = response.url.split('/')[-1]
            item['path'] = item['fileName'] + '/'+ str(i) + '.jpg'
            item['pageURL'] = pageURL + '/' + str(i)
            items.append(item)

        for item in items:
            yield Request(url=item['pageURL'],meta={'item2':item},callback=self.parse_two)

    def parse_two(self,response):
        # pass
        item = MziItem()
        item3 = response.meta['item2']

        URL = response.xpath('//div[@class="main-image"]//img/@src').extract()[0]
        item['image_urls'] = URL
        item['path'] = item3['path']
        item['fileName'] = item3['fileName']
        print 'result is :-->' + item['image_urls'],item['path'],item['fileName']

        yield item



        
