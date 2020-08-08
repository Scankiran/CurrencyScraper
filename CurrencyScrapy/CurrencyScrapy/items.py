# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CurrencyscrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    value = scrapy.Field()
    diferency = scrapy.Field()
    type = scrapy.Field()


class BankValueItem(scrapy.Item):

    bankName = scrapy.Field()
    values = scrapy.Field()
    difference = scrapy.Field()
