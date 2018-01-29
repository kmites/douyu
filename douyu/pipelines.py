# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
#导入图片设置的存储路径
from douyu.settings import IMAGES_STORE as images_store
import os
import scrapy
#导入图片处理管道
from scrapy.pipelines.images import ImagesPipeline

class DouyuPipeline(ImagesPipeline):

    def get_media_requests(self,item,info):
        image_src = item["image_src"]
        #下载图片
        yield scrapy.Request(image_src)

    def item_completed(self, results, item, info):

        #取得图片的名称
        image_path = [x['path'] for ok,x in results if ok]
        #重命名
        os.rename(images_store+image_path[0],images_store+item['nick_name']+'.jpg')


