# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BasketballItem(scrapy.Item):
	player = scrapy.Field()
	year_min = scrapy.Field()
	height = scrapy.Field()
	weight = scrapy.Field()
