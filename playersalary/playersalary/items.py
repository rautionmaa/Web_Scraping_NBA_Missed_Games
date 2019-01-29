# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PlayerSalaryItem(scrapy.Item):
    player = scrapy.Field()
    player_salary = scrapy.Field()
    season = scrapy.Field()
