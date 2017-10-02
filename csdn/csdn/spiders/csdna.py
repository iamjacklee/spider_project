# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from csdn.items import CsdnItem
from scrapy.selector import Selector


class CsdnaSpider(CrawlSpider):
    name = 'csdna'
    allowed_domains = ['blog.csdn.net']
    start_urls = ['http://blog.csdn.net/peihaozhu/article/list/1',]

    rules = (
        Rule(LinkExtractor(allow=r'/peihaozhu/article/list/\d+'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        
        sel = response.selector
        posts = sel.xpath('//*[@id="article_list"]/div[@class="list_item article_item"]')
        items = []
        
        for p in posts:
            item = CsdnItem()
            item['title'] = p.xpath('.//span[@class="link_title"]/a/text()').extract_first()
            item['pdate'] = p.xpath('.//span[@class="link_postdate"]/text()').extract_first()
            item['url'] = response.url
            item['description'] = p.xpath('.//*[@class="article_description"]/text()').extract_first()
            
            items.append(item)
            
            
        return items
