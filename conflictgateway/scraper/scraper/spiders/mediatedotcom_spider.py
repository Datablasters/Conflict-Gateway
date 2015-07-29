#!/usr/bin/env python

import scrapy
from scraper.items import NewsItem
from scraper.media import uploadImg
import datetime

class MediateDotComSpider(scrapy.Spider):
    name = 'mediatedotcom'
    allowed_domains = ['mediate.com']
    start_urls = [
                  "http://www.mediate.com/today/",
                 ]
    
    def parse(self, response):
        thumbs = []
        titles=[]
        taglines=[]
        websites=[]
        links=[]

        for sel in response.xpath('//ul[not(@id)]/li'):
            try:
                title_item = str(sel.xpath("a/strong/text()").extract()[0].encode('ascii', 'ignore'))
                website_item = str(sel.xpath("a/@href").extract()[0].encode('ascii', 'ignore')).split("/")[2][4:]
                website_itemb = str(sel.xpath("a/@href").extract()[0].encode('ascii', 'ignore'))
                tagline_item = str(sel.xpath("p/text()").extract()[0].encode('ascii', 'ignore'))[:320]
            except:
                title_item = "#"
                website_item = "#"
                website_itemb = "#"
                tagline_item = "#"

            titles.append(title_item)
            websites.append(website_item)
            links.append(website_itemb)
            taglines.append(tagline_item)

        for sel in response.xpath('//ul[not(@id)]/img'):
            thumb_item = str(sel.xpath("@src").extract()[0].encode('ascii', 'ignore'))
            thumbs.append(thumb_item)

        for x in range (len(titles)):
            if links[x] == "#":
                pass
            else:
                item = NewsItem()
                item['title'] = titles[x]
                item['articletype'] = "News"
                item['tags'] = "news"
                item['thumbnail'] = uploadImg(thumbs[x])
                item['tagline'] = taglines[x]
                item['website'] = websites[x]
                item['link'] = links[x]
                item['created'] = datetime.date.today()
                item['hits'] = 0
                item['user_id'] = 1
                yield item

        print "Titles: " + str(len(titles))
        print "Thumbs: " + str(len(thumbs))
        print "Taglines: " + str(len(taglines))
        print "Websites: " + str(len(websites))
        print "Links: " + str(len(links))

