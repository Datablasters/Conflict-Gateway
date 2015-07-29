#!/usr/bin/env python

import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scraper.items import JobsItem
from scraper.media import uploadImg
import datetime
from django.utils.text import slugify

class FindAPhDSpider(CrawlSpider):
    name = 'unjobs'
    allowed_domains = ['unjobs.org']
    start_urls = [
                  "http://unjobs.org/themes/conflict-resolution",
                 ]
    rules = (Rule(LinkExtractor(allow=('vacancies'),), callback="parse_items", follow=False),)
    
    def parse_items(self, response): 
        try:
            title = response.xpath("//h1/text()").extract()
            link = response.url
            location = response.xpath('//strong[contains(text(), "Location :")]/following-sibling::text()[1]').extract()
            tagline = ""
            body = response.xpath('//p').extract()
            body = ''.join(body).encode('ascii','ignore')
            
            item = JobsItem()
            item['articletype'] = "Jobs"
            item['title'] = str(title[0]).encode('ascii', 'ignore')
            item['title_slug'] = slugify(title[0]).encode('ascii', 'ignore')
            item['created'] = datetime.date.today()
            item['author'] = "Apply Online"
            item['authorimg'] = "jobs.png"
            item['hits'] = 0
            item['tags'] = "Jobs, UN"
            try:
                item['location'] = str(location[0]).encode('ascii', 'ignore')
            except:
                item['location'] = "Unknown"
            item['salary'] = "Unknown"
            item['thumbnail'] = "un.jpg"
            item['image'] = "un.jpg"
            item['tagline'] = tagline
            item['body'] = body
            item['link'] = str(link).encode('ascii', 'ignore')
            item['user_id'] = 1
            item['urlsection'] = "jobs"
            return item
        except:
            print "Cannot parse page"
           

