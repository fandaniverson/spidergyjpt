# -*- coding: utf-8 -*-
import scrapy
from gyjpt.items import GyjptItem
from scrapy.selector import Selector
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class ChanpcrawlSpider(scrapy.Spider):
    name = 'chanpcrawl'
    allowed_domains = ['http://www.gdyjs.cn/UserService/ProductList.aspx']
    start_urls = ['http://www.gdyjs.cn/UserService/ProductList.aspx/']

    def parse(self, response):
        e=[]
        tr=response.xpath("//table[@align='center']/tr[not(@class='header')]").extract()
        for i in tr:
            g = GyjptItem()
            c=Selector(text=i).xpath("//tr/td/text()").extract()
            g['protduct_name']=c[0]
            g['goods_name']=c[1]
            g['product_location']=c[2]
            g['product_xing']=c[3]
            g['product_desc']=c[4]
            e.append(g)
        return e
