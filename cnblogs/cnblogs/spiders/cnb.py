# -*- coding: utf-8 -*-
import scrapy
from cnblogs.items import CnblogsItem

class CnbSpider(scrapy.Spider):
    name = 'cnb'
    # allowed_domains = ['cnblog.com']
    # start_urls = ['http://www.cnblogs.com/qiyeboy/default.html?page=1']
    start_urls = ['http://www.cnblogs.com/qiyeboy/default.html?page={}'.format(i) for i in range(1,6)]


    def parse(self, response):
        # pass
        papers = response.xpath('//div[@class="day"]')
        # items = {}
        for paper in papers:
            item = CnblogsItem()
            item['title'] = paper.xpath('./div[@class="postTitle"]/a/text()').extract()[0]
            item['day'] = paper.xpath('./div[@class="dayTitle"]/a/text()').extract()[0]
            item['postcon'] = paper.xpath('./div[@class="postCon"]/div[@class="c_b_p_desc"]/text()').extract()[0]
            yield item
            # items.append(item)
        # yield items

            # print title,day
            # print poscon
            # print title
            # i = i+1
        # print i
