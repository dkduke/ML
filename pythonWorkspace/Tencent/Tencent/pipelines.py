# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class TencentPipeline(object):

    def __init__(self):
        self.f=open('tencent.json',"w")

    def process_item(self, item, spider):
        #因为json.dumps 序列化时对中文默认使用的ascii编码,想输出真正的中文需要指定ensure_ascii=False
        content=json.dumps(dict(item),ensure_ascii=False)+",\n"
        self.f.write(content)
        return item

    def close_spider(self,spider):
        self.f.close()
