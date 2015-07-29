#!/usr/bin/env python

import scrapy
from scraper.items import NewsItem
from scraper.media import uploadImg
import datetime

class ScienceDailySpider(scrapy.Spider):
    name = 'sciencedaily'
    allowed_domains = ['sciencedaily.com']
    start_urls = [
                  "http://www.sciencedaily.com/terms/conflict_resolution.htm",
                 ]
    
    def parse(self, response):         
        title = response.xpath("//div[@class='search_headlines']/h3/a/text()").extract()
        tagline = response.xpath("//div[@class='search_headlines']/div/text()").extract()
        link = response.xpath("//div[@class='search_headlines']/h3/a/@href").extract()
        #cleanse tagline data
        new_tagline = []
        for x in tagline:
            if x != "\n":
                new_tagline.append(x)
        
        for x in range(len(title)):
            try:
                item = NewsItem()
                item['title'] = title[x].encode('ascii','ignore')
                item['articletype'] = "News"
                item['tags'] = "news"
                item['thumbnail'] = "sciencedaily.png"
                item['tagline'] = new_tagline[x].encode('ascii','ignore') 
                item['website'] = "Sciencedaily.com"
                item['link'] = "http://www.sciencedaily.com" + str(link[x].encode('ascii','ignore'))
                item['created'] = datetime.date.today()
                item['hits'] = 0
                item['user_id'] = 1
                yield item
            except:
                pass
                
        print "Titles: " + str(len(title))
        print "Taglines: " + str(len(new_tagline))
        print "Links: " + str(len(link))




