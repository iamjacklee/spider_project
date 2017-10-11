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


    def parse_one(self,response):
        # pass
        item2 = response.meta['item1']
        # source = requests.get(response.url)
        # html = source.text.encode('utf-8')

        num = response.xpath('//div[@class="pagenavi"]/a/span/text()').extract()[-2]
        pageURL = response.url
        items = []
        # print 'num is :--->' + num
        # print 'pageURL:--->' + pageURL
        # print 'filename :--->' +item2['fileName']

        for i in range(1,int(num)+1):
            item = MziItem()
            item['fileName'] = item2['fileName']
            # item['path'] = response.url.split('/')[-1]
            item['path'] = item['fileName'] + '/'+ str(i) + '.jpg'
            item['pageURL'] = pageURL + '/' + str(i)

            # if int(i) == 1:
            #     item['pageURL'] = pageURL
            #     print 'pagenum is **************************' + item['pageURL']             
            # else:
            #     item['pageURL'] = pageURL + '/' + str(i)
                

            items.append(item)
            # if int(i)==1:
            #     print 'pageURL is 1----------->' + item['pageURL']

        for item in items:
            yield Request(url=item['pageURL'],dont_filter=True,meta={'item2':item},callback=self.parse_two)
            # yield Request(url=item['pageURL'],meta={'item2':item,'dont_redirect': True,'handle_httpstatus_list': [301]},callback=self.parse_two)

    def parse_two(self,response):
        # pass
        item = MziItem()
        item3 = response.meta['item2']
        # urlstr = response.url.split('/')
        # pagenum = urlstr[-1]
        # print 'pagenum is **************************' + pagenum

                # if pagenum=='1':
            #     print 'response.url is 1----------------------------------->' + response.url
        #     newurl = urlstr[0] +'//' + urlstr[2] + '/' + urlstr[3]
        #     URL = newurl.xpath('//div[@class="main-image"]//img/@src').extract()[0]
        # else:            
        #     URL = response.xpath('//div[@class="main-image"]//img/@src').extract()[0]
        # if pagenum=='1':
        #     response.url = urlstr[0] +'//' + urlstr[2] + '/' + urlstr[3]


        URL = response.xpath('//div[@class="main-image"]//img/@src').extract()[0]

        item['image_urls'] = URL
        item['path'] = item3['path']
        item['fileName'] = item3['fileName']
        # print 'result is :-->' + item['image_urls'],item['path'],item['fileName']

        yield item



        
