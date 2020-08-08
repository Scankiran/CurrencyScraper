# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

import scrapy
from ..items import CurrencyscrapyItem
from ..items import BankValueItem


class QuotesSpider(scrapy.Spider):
    name = "currency"
    start_urls = [
        'https://kur.doviz.com/serbest-piyasa/euro'
    ]


    def parse(self, response):

        for quote in response.css('div.item'):
            item = CurrencyscrapyItem()
            diffValue = quote.css('a div::text').extract_first()
            clearDiffValue = ""

            diff = "Up"
            for char in diffValue:
                if char != "\'" and char != "n" and char != " ":
                    clearDiffValue = clearDiffValue + char
                if char == '-':
                    diff = "Down"

                item['title'] = quote.css('a span.name::text').extract_first()
                item['value'] = quote.css('a span.value::text').extract_first()
                item['type'] = diff
                item['diferency'] = clearDiffValue

            yield item



class EuroSpider(scrapy.Spider):
    name = 'euro'
    start_urls = [
        'https://kur.doviz.com/serbest-piyasa/euro'

    ]

    def parse(self, response):
        item = CurrencyscrapyItem()
        print('red')
        for quote in response.css('tbody tr'):
            yield {
                'Name': quote.css('td a::text').extract_first(),
                'sellVal': quote.css('td.text-bold::text').extract(),
                # 'diff': quote.css('td span.ml-2 span::text').extract_first(),
            }



