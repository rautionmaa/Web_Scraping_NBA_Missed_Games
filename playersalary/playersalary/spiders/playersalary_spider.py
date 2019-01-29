# This spider scraped hoopshype for player salary
# Player salary data only goes back to 2000
# year_end is dictionary of years
# Suffix created year pair (2001-2002) to start_url.


from scrapy import Spider
from playersalary.items import PlayerSalaryItem
year_end = [2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]
suffix = [str(year_end[i] - 1) + "-" + str(year_end[i]) for i in range(len(year_end))]

class playersalaryspider(Spider):
	name = "playersalary_spider"
	allowed_urls = ['https://hoopshype.com']
	start_urls = ['https://hoopshype.com/salaries/players/' + s for s in suffix]

	def parse(self, response):
		rows = response.xpath('//*[@id="content-container"]/div/div[3]/div[2]')
		player = response.xpath('//td[@class="name"]/a/text()').extract()
		player_salary = response.xpath('//tbody/tr/td[3]/text()').extract()
		season = response.xpath('//table/thead/tr/td[3]/text()').extract()

# Strip \n and \t from player bame and season

		player = list(map(lambda x: x.strip('\n\t'), player))
		player_salary = list(map(lambda x: x.strip(), player_salary))
		season = list(map(lambda x: x.strip('\n\t'), season))
		print(player)
		print(player_salary)
		print(season)


		print("+"*50)
		print(len(rows))

# Loop through every player and salary on every page
# Take season only once per page

		for r in range(0, len(player_salary)):
			item = PlayerSalaryItem()
			item['player'] = player[r]
			item['player_salary'] = player_salary[r]
			item['season'] = season
			yield item