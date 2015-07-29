# -*- coding: utf-8 -*-

# Scrapy settings for cgscraper project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'scraper'

SPIDER_MODULES = ['scraper.spiders']
NEWSPIDER_MODULE = 'scraper.spiders'
ITEM_PIPELINES = {'scraper.pipelines.NewsPipeline': 100, 'scraper.pipelines.JobsPipeline': 200}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'cgscraper (+http://www.yourdomain.com)'

DATABASE = {
    'drivername': 'postgres',
    'host': 'HOST',
    'port': '5432',
    'username': 'USER',
    'password': 'PASSWORD',
    'database': 'DBNAME'
}
# Database settings to connect to PostGresSql AWS database.


