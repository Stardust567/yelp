# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from yelp.items import YelpItem

class ReviewSpider(scrapy.Spider):
    name = 'Review'
    allowed_domains = ['yelp.com']
    base_url = 'https://www.yelp.com/search?cflt=restaurants&find_loc=Austin%2C%20TX'
    start_urls = []
    for number in range(0, 600, 30): # 爬取个870个店
        url = base_url + '&start=' + str(number)
        start_urls.append(url)

    def parse(self, response):
        urls = response.css('li').css('h3').css('a').xpath('@href').extract()
        for url in urls: # 每个https://www.theguardian.com/uk/sport/2019/apr/01/all页面上的news连接
            url = 'https://www.yelp.com' + url
            print(url)
            yield Request(url, self.get_review)

    def get_review(self, response):
        item = YelpItem()
