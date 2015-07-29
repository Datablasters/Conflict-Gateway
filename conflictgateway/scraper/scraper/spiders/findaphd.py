#!/usr/bin/env python

import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scraper.items import JobsItem
from scraper.media import uploadImg
import datetime
from django.utils.text import slugify

class FindAPhDSpider(CrawlSpider):
    name = 'findaphd'
    allowed_domains = ['findaphd.com']
    start_urls = [
                  "http://www.findaphd.com/search/phd.aspx?DID=13&Keywords=conflict+resolution",
                 ]
    rules = (Rule(LinkExtractor(allow=('search/ProgrammeDetails','search/ProjectDetails','search/PhDDetails' ),), callback="parse_items", follow=False),)
    
    def parse_items(self, response): 
        try:        
            title = response.xpath("//a[@id='hlTitle']/text()").extract()
            link = response.xpath("//a[@id='hlTitle']/@href").extract()
            location = response.xpath("//a[@id='hlInstitution']/text()").extract()
            tagline = ""
            body = response.xpath("//div[@id='itemDescription']").extract()
            
            item = JobsItem()
            item['articletype'] = "Jobs"
            item['title'] = "PhD | " + str(title[0]).encode('ascii','ignore')
            item['title_slug'] = slugify(title[0]).encode('ascii','ignore')
            item['created'] = datetime.date.today()
            item['author'] = "Apply Online"
            item['authorimg'] = "jobs.png"
            item['hits'] = 0
            item['tags'] = "Jobs, PhD, Scholarship"
            item['location'] = str(location[0]).encode('ascii','ignore')
            item['salary'] = "Scholarship"
            item['thumbnail'] = "findaphd.png"
            item['image'] = "findaphd.jpg"
            item['tagline'] = tagline
            item['body'] = body[0]
            item['link'] = str(link[0]).encode('ascii','ignore')      
            item['user_id'] = 1
            item['urlsection'] = "jobs"
            return item
        except:
            print "Cannot parse page"
           

