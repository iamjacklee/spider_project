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

class MziPipeline(object):
    def process_item(self, item, spider):
        # return item
        detailURL = item['detailURL']
        path = item['path']
        fileName = item['fileName']

        if not os.path.exists(fileName):
            os.makedirs(fileName)

        image = requests.get(detailURL)
        f = open(path,'wb')
        f.write(image.content)
        f.close()

        return item
