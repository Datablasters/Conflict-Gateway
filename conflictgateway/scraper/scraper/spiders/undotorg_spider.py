#!/usr/bin/env python

import scrapy
from scraper.items import NewsItem
from scraper.media import uploadImg
import datetime

class UNSpider(scrapy.Spider):
    name = 'undotorg'
    allowed_domains = ['un.org']
    start_urls = [
                  "http://www.un.org/en/peacekeeping/news/",
                 ]
    
    def parse(self, response):         
        title = response.xpath("//div[@id='text']/div/a/text()").extract()
        thumbnail = response.xpath("//div[@id='text']/div/img/@src").extract()
        tagline = response.xpath("//div[@id='text']/div/p/text()").extract()
        link = response.xpath("//div[@id='text']/div/a/@href").extract()
  
        for x in range(10):
            try:
                item = NewsItem()
                item['title'] = title[x].encode('ascii','ignore')
                item['articletype'] = "News"
                item['tags'] = "news"
                item['thumbnail'] = uploadImg(thumbnail[x])
                item['tagline'] = tagline[x].encode('ascii','ignore') 
                item['website'] = "un.org"
                item['link'] = "http://www.un.org" + str(link[x].encode('ascii','ignore'))
                item['created'] = datetime.date.today()
                item['hits'] = 0
                item['user_id'] = 1
                yield item
            except:
                pass
                
        print "Titles: " + str(len(title))
        print "Thumbs: " + str(len(thumbnail))
        print "Taglines: " + str(len(tagline))
        print "Links: " + str(len(link))
    



