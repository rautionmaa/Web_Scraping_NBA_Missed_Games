# This spider scraped basketball reference's all players page
# By alphabetical order. Scrapes player name, first year, height and weight

from scrapy import Spider
from basketball.items import BasketballItem
import string

#lower case alphabet (start_url code skips letter x. No x last names)
alphabet = list(string.ascii_lowercase)

class basketballspider(Spider):
	name = "basketball_spider"
	allowed_urls = ['https://www.basketball-reference.com/']
	start_urls = ['https://www.basketball-reference.com/players/' + x for x in alphabet if x!='x']

	def parse(self, response):
		rows = response.xpath('//table[@id="players"]//tr')
		player = response.xpath('//*[@id="players"]/tbody/tr/th//a/text()').extract()
		year_min = response.xpath('//*[@id="players"]/tbody/tr/td[1]/text()').extract()
		height = response.xpath('//*[@id="players"]/tbody/tr/td[4]/text()').extract()
		weight = response.xpath('//*[@id="players"]/tbody/tr/td[5]/text()').extract()

		print("+"*50)
		print(len(player))

# Grab every player, year_min, height and weight on the page, then move onto next page
		for i in range(0, len(player)):
			item = BasketballItem()
			item['player'] = player[i]
			item['year_min'] = year_min[i]
			item['height'] = height[i]
			item['weight'] = weight[i]

			yield item

