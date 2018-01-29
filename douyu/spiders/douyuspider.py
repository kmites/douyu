# -*- coding: utf-8 -*-
import scrapy
import json
from douyu.items import DouyuItem


class DouyuspiderSpider(scrapy.Spider):
    name = 'douyuspider'
    allowed_domains = ['douyucdn.cn']
    baseURL = 'http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset='
    offset = 0
    start_urls = [baseURL+str(offset)]

    def parse(self, response):

        data_list = json.loads(response.body.decode('utf-8'))['data']

        if len(data_list)==0:
            return

        for data in data_list:
            item = DouyuItem()
            item["nick_name"] = data["nickname"]
            item["image_src"] = data["vertical_src"]
            yield item

        self.offset += 20
        url = self.baseURL+str(self.offset)
        yield scrapy.Request(url,callback=self.parse)

