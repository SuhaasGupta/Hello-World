# -*- coding: utf-8 -*-
import scrapy


class BirtcountrySpider(scrapy.Spider):
    name = 'birtcountry'
    allowed_domains = ['suhas.com']
    start_urls = ['https://en.wikipedia.org/wiki/David_Warner_(cricketer)', 'https://en.wikipedia.org/wiki/Virat_Kohli's]

    def parse(self, response):
        yield{
            'name':response.css('span.fn::text').extract(),
            'country':response.css('span.birthplace::text').extract()

            
            }
