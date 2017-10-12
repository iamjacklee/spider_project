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
import pymongo
# from mzi.settings import settings
from scrapy.conf import settings


class MziPipeline(object):

    def __init__(self):
        host = settings['MONGODB_HOST']
        port = settings['MONGODB_PORT']
        dbName = settings['MONGODB_DBNAME']
        col = settings['MONGODB_DOCNAME']
        client = pymongo.MongoClient(host=host,port=port)
        tdb = client[dbName]        
        self.post = tdb[col]

    def process_item(self, item, spider):
        # return item
        article = dict(item)
        self.post.insert(article)

        return item



class MyImagesPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            yield scrapy.Request(image_url, meta={'item': item},headers={'Referer':image_url})
        

        # image_url = item['image_urls']
        # yield scrapy.Request(image_url, meta={'item': item},headers={'Referer':image_url})

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        # else:

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
