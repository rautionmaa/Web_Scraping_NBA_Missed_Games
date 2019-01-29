# This spider scrapes realgm.com for player, team, games played, minutes, season
# Every season/year has 4 pages 
# year_end adds year to middle of URL
# page_number adds page number to middle of URL

from scrapy import Spider
from scrapy import Request
import re
from games_missed.items import GamesMissedItem
year_end = [1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]
page_number = [1, 2, 3, 4]
year_end_choice = [str(year_end[y]) for y in range(len(year_end))]
page_number_choice = [str(page_number[p]) for p in range(len(page_number))]
url_list = []
for y in year_end_choice:
    for p in page_number_choice:
        url_list.append('https://basketball.realgm.com/nba/stats/{}/Averages/Qualified/player/All/asc/{}/Regular_Season'.format(y,p))

class games_missedspider(Spider):
	name = "games_missed_spider"
	allowed_urls = ['https://basketball.realgm.com']
	start_urls = ['https://basketball.realgm.com/nba/stats/1999/Averages/Qualified/player/All/asc/1/Regular_Season']


	def parse(self, response):
		for url in url_list:
			yield Request(url=url, callback=self.parseresults)

	def parseresults(self, response):		
		player = response.xpath('//tbody/tr/td[2]/a/text()').extract()
		team = response.xpath('//tbody/tr/td[3]/text()').extract()
		games_played = response.xpath('//tbody/tr/td[4]/text()').extract()
		minutes_per_game = response.xpath('//tbody/tr/td[5]/text()').extract()
		season = str(response.xpath('//div[3]/div/h2[3]/text()').extract())

		print("+"*50)

# Scrape evry olayer, team, games, minutes on every page
# scrape only season once but join with a -

		for i in range(0, len(player)):
			item = GamesMissedItem()
			item['player'] = player[i]
			item['team'] = team[i]
			item['games_played'] = games_played[i]
			item['minutes_per_game'] = minutes_per_game[i]
			item['season'] = "-".join(re.findall("\d+", season))
			yield item