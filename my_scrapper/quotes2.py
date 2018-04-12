# -*- coding: utf-8 -*-
import scrapy


class Quotes2Spider(scrapy.Spider):
    name = 'quotes2'
    #allowed_domains = ['suhas.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        for each in response.css('div.quote'):
            yield {
                     'quote': each.css('div.quote > span.text::text').extract(),
                     'author': each.css('div.quote > span >small.author::text').extract()
                     }
            
        relative_url = response.css('li.next > a::attr(href)').extract_first()
        full_url = response.urljoin(relative_url)
        yield scrapy.Request(url=full_url, callback = self.parse)
        

