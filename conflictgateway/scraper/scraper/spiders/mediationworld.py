#!/usr/bin/env python

import scrapy
from scraper.items import NewsItem
from scraper.media import uploadImg
import datetime

class MediationWorldSpider(scrapy.Spider):
    name = 'mediationworld'
    allowed_domains = ['mediationworld.com']
    start_urls = [
                  "http://www.mediationworld.net/news-developments/news.html",
                 ]
    
    def parse(self, response):         
        title = response.xpath("//div[@id='mainright']/a/b/text()").extract()
        tagline = response.xpath("//div[@id='mainright']/p/text()").extract()
        link = response.xpath("//div[@id='mainright']/a[@class='main']/@href").extract()
        new_tagline = []
        for x in tagline:
            if len(x) > 15:
                new_tagline.append(x)
        for x in range(5):
            try:
                item = NewsItem()
                item['title'] = title[x].encode('ascii','ignore')
                item['articletype'] = "News"
                item['tags'] = "news"
                item['thumbnail'] = "mediationworld.png"
                item['tagline'] = new_tagline[x].encode('ascii','ignore') 
                item['website'] = "mediationworld.net"
                item['link'] = "http://www.mediationworld.net" + str(link[x].encode('ascii','ignore'))
                item['created'] = datetime.date.today()
                item['hits'] = 0
                item['user_id'] = 1
                yield item
            except:
                pass
                
        print "Titles: " + str(len(title))
        print "Taglines: " + str(len(new_tagline))
        print "Links: " + str(len(link))
        
        for x in new_tagline:
            print "***" + x + "\n" + str(len(x))



