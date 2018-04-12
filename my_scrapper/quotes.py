# -*- coding: utf-8 -*-
import scrapy


    class QuotesSpider(scrapy.Spider):
        name = 'quotes'
        start_urls = ['http://quotes.toscrape.com/']
    

        def parse(self, response):

            for each in response.css('div.quote'):
                yield{
            
                    'quote': each.css('span.text::text').extract(),
                    'author': each.css('small.author::text').extract()

                }

           
