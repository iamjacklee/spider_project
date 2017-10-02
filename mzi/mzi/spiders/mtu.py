# -*- coding: utf-8 -*-
import scrapy
from mzi.items import MziItem


class MtuSpider(scrapy.Spider):
    name = 'mtu'
    allowed_domains = ['mzitu.com']
    start_urls = ['http://mzitu.com/all']

    def parse(self, response):
        # pass
        # print response.text
        # pages = response.xpath('//*[@class="all"]//ul')
        pages = response.xpath('//*[@class="all"]//ul//li//p[@class="url"]/a')
        items = []
        item = MziItem()
        for page in pages:
            
            # item['img_name'] = page.xpath('.//p[@class="url"]/a/text()').extract()[0]
            # item['page_url'] = page.xpath('.//p[@class="url"]/a/@href').extract()[0]

            item['img_name'] = page.xpath('./text()').extract()
            item['page_url'] = page.xpath('./@href').extract()

            # items.append(item)
            yield item

        # print items
        # yield items
