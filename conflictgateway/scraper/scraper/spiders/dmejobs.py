#!/usr/bin/env python

import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scraper.items import JobsItem
from scraper.media import uploadImg
import datetime
from django.utils.text import slugify
import re

class FindAPhDSpider(CrawlSpider):
    name = 'dmejobs'
    allowed_domains = ['dmeforpeace.org']
    start_urls = [
                  "http://www.dmeforpeace.org/opportunities/jobs",
                 ]
    rules = (Rule(LinkExtractor(allow=('opportunities/jobs')), callback="parse_items", follow=False),)
    
    def parse_items(self, response): 
        try:
            title = response.xpath('//div[@class="jobs_container"]/h2/a/text()').extract()
            link = response.xpath('//div[@class="links"]/div/div/div/a/@href').extract()
            location = response.xpath('//div[@class="organization"][1]/div/div/div//text()').extract()
            tagline = response.xpath('//div[@class="content"]/div/div/div/p/span/text()').extract()
            body = response.xpath('//div[@class="jobs_container"]').extract()
            item = JobsItem()
            item['articletype'] = "Jobs"
            item['title'] = str(title[0]).encode('ascii', 'ignore')
            item['title_slug'] = slugify(title[0]).encode('ascii', 'ignore')
            item['created'] = datetime.date.today()
            item['author'] = "Apply Online"
            item['authorimg'] = "jobs.png"
            item['hits'] = 0
            item['tags'] = "Jobs"
            item['location'] = str(location[0]).encode('ascii', 'ignore')
            item['salary'] = "N/A"
            item['thumbnail'] = "job.jpg"
            item['image'] = "job.jpg"
            try:
                tagline = tagline[0].encode('ascii', 'ignore')
                item['tagline'] = tagline[0:100]
            except:
                item['tagline'] = ""
            if len(item['tagline']) < 30:
                item['tagline'] = ""

            #Remove links from body text
            pattern =r'<(a|/a).*?>'
            body = body[0].encode('ascii', 'ignore')
            item['body'] = re.sub(pattern, "", body)
            try:
                item['link'] = str(link[0]).encode('ascii','ignore')
            except:
                item['link'] = ""
            item['user_id'] = 1
            item['urlsection'] = "jobs"
            return item
        except:
            print "Cannot parse page"

