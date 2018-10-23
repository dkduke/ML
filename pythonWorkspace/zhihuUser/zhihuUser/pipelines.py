# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

#  管道文件的作用只有一个，处理item字段的

import json


class ZhihuuserPipeline(object):
    def __int__(self):
        self.f=open("itcast_pipeline.json",'w')

    def process_item(self, item, spider):
        content=json.dump(dict(item),ensure_ascii=False)+',\n'
        content.f.write(item.enconde('utf-8'))
        return item


    def close_spider(self,spider):
        pass
