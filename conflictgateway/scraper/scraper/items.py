# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NewsItem(scrapy.Item):
    articletype = scrapy.Field()
    title = scrapy.Field()
    tags = scrapy.Field()
    thumbnail = scrapy.Field()
    tagline = scrapy.Field()
    website = scrapy.Field()
    link = scrapy.Field()
    created = scrapy.Field()
    hits = scrapy.Field()
    user_id = scrapy.Field()

class JobsItem(scrapy.Item):
    articletype = scrapy.Field()
    title = scrapy.Field()
    title_slug = scrapy.Field()
    created = scrapy.Field()
    author = scrapy.Field()
    authorimg = scrapy.Field()
    hits = scrapy.Field()
    tags = scrapy.Field()
    location = scrapy.Field()
    salary = scrapy.Field()
    thumbnail = scrapy.Field()
    image = scrapy.Field()
    tagline = scrapy.Field()
    body = scrapy.Field()
    link = scrapy.Field()
    user_id = scrapy.Field()
    urlsection = scrapy.Field()
