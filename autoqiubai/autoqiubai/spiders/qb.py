# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from autoqiubai.items import AutoqiubaiItem
from scrapy.http import Request

class QbSpider(CrawlSpider):
    name = 'qb'
    allowed_domains = ['qiushibaike.com']
    '''
    start_urls = ['http://qiushibaike.com/']
    '''
    def start_requests(self):
        ua={"User-Agent":'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
        yield Request('http://www.qiushibaike.com/',headers=ua)
    rules = (
        Rule(LinkExtractor(allow='article'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        i=AutoqiubaiItem()
        i['content'] = response.xpath("//div[@class='content']/text()").extract()
        i['link'] = response.xpath("//link[@rel='canonical']/@href").extract()
        return i
