# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import requests
import sys
import os
reload(sys)
sys.setdefaultencoding('utf-8')
import scrapy
from scrapy.pipelines.images import ImagesPipeline


# class MziPipeline(object):
#     def process_item(self, item, spider):
#         # return item
#         detailURL = item['detailURL']
#         path = item['path']
#         fileName = item['fileName']

#         if not os.path.exists(fileName):
#             os.makedirs(fileName)

#         image = requests.get(detailURL)
#         f = open(path,'wb')
#         f.write(image.content)
#         f.close()

#         return item



class MyImagesPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        # for image_url in item['image_urls']:
        # print 'image_url is :--->' + image_url
        # yield scrapy.Request(image_url, meta={'item': item},headers={'Referer':'http://www.mzitu.com/1/3',"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"})
        image_url = item['image_urls']
        yield scrapy.Request(image_url, meta={'item': item},headers={'Referer':image_url})

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        return item

    def file_path(self, request, response=None, info=None):
        item = request.meta['item']
        name = item['path']
        # folder = item['fileName']
        # print 'foderName is :--->' + folder
        # if not os.path.exists(folder):
        #     os.makedirs(folder)
        
        filename = u'{0}'.format(name)
        return filename 
