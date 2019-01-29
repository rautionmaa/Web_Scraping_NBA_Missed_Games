# This spider scrapes NBA wikipedia page for games per season.
# Most recent season have 82 games, a few have less because of lockout season

from scrapy import Spider
from basketballgames.items import BasketballGamesItem

class basketballgamesspider(Spider):
	name = "basketballgames_spider"
	allowed_urls = ['https://en.wikipedia.org/wiki/Main_Page']
	start_urls = ['https://en.wikipedia.org/wiki/List_of_National_Basketball_Association_seasons']

	def parse(self, response):
		rows = response.xpath('//*[@id="mw-content-text"]/div/table/tbody/tr')
		seasons = response.xpath('//*[@id="mw-content-text"]/div/table/tbody/tr/td[1]/a/text()').extract()
		total_games = response.xpath('//*[@id="mw-content-text"]/div/table/tbody/tr/td[10]/text()').extract()

		print("+"*50)
		print(len(rows))

# Grab every season and total games on the table

		for i, total_game in enumerate(total_games):
			item = BasketballGamesItem()
			item['season'] = seasons[i]
			item['total_games'] = total_games[i]
			yield item 
