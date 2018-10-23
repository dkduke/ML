# -*- coding: utf-8 -*-
# import scrapy
#
#
# class ZhihuSpider(scrapy.Spider):
#     name = 'zhihu'
#     allowed_domains = ['www.zhihu.com']
#     start_urls = ['http://www.zhihu.com/']
#
#     def parse(self, response):
#         pass

import scrapy

from zhihuUser.items import ZhihuuserItem

class ZhihuSpider(scrapy.Spider):
    name = 'zhihu'  #启动爬虫时会按照爬虫名启动
    #爬虫的爬取域范围
    allowed_domains = ['http://www.itcast.cn']
    #起始url列表
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    #用于解析，名字固定
    def parse(self, response):
        #file_name='teacher.html'
        #open(file_name,'wb').write(response.body)

        items=[]

        node_list=response.xpath('//div[@class="li_txt"] ')

        for site in node_list:

            item=ZhihuuserItem()

            teacher_name=site.xpath('h3/text()').extract()
            teacher_leave=site.xpath('h4/text()').extract()
            teacher_info =site.xpath('p/text()').extract()

            # print (teacher_name[0])
            # print(teacher_leave[0])
            # print(teacher_info[0])
            # print("*"*30)

            item['name']=teacher_name[0]
            item['leave']=teacher_leave[0]
            item['info']=teacher_info[0]

            #yield返回提取到的每一个item数据，给管道文件处理，同时还回来继续执行后面的代码
            yield item


            # 这个返回给引擎，引擎去判断是item字段的话返回给管道，判断是请求时会返回给调度器
            #return item  #item字段
            #return scrapy.Request(url)  #请求



            # items.append(item)

        #返回item文件，-o可生成xml，json，csv文件
        # return items

