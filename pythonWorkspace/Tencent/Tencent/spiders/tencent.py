# -*- coding: utf-8 -*-
import scrapy

from ..items import TencentItem

class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['tencent.com']
    base_URL = 'https://hr.tencent.com/position.php?keywords=&lid=2175&start='
    #https://hr.tencent.com/position.php?keywords=&lid=2175&tid=87&start=0#a



    offset=10

    start_urls=[base_URL+str(offset)+'#a']


    def parse(self, response):
        pass

        node_list=response.xpath("//tr[@class='even']|//tr[@class='odd']")

        for node in node_list:
            item=TencentItem()

            item['positionName']=node.xpath('./td[1]/a/text()').extract()[0]

            if len(node.xpath('./td[1]/a/@href')):
                item['positionLink'] = node.xpath('./td[1]/a/@href').extract()[0]
            else:
                item['positionLink']=''

            if len(node.xpath('./td[2]/text()')):
                item['positionType'] = node.xpath('./td[2]/text()').extract()[0]
            else:
                item['positionType']=''

            item['peopleNumber'] = node.xpath('./td[3]/text()').extract()[0]

            item['workLocation'] = node.xpath('./td[4]/text()').extract()[0]

            item['publishTime'] = node.xpath('./td[5]/text()').extract()[0]

            yield item
            #拼接url，获取下一个url，这种获取方法并不好
            # if self.offset<40:
            #     self.offset += 10
            #     url=self.base_URL+str(self.offset)+'#a'
            #     yield scrapy.Request(url,callback=self.parse)


            #第二种写法，直接从responese中获取爬取的链接，并且发送请求处理，直到链接全部提取完
            #注意if停止条件在最后一页与前面页对比，找不同
            if len(response.xpath('//a[@class="noactive" and @id="next"]'))==0:
                print("*"*150)
                foot_url=response.xpath('//a[@id="next"]/@href').extract()[0]

                url="https://hr.tencent.com/"+foot_url
                yield  scrapy.Request(url,callback=self.parse)




    # def pase_next (self,response):
    #     pass

