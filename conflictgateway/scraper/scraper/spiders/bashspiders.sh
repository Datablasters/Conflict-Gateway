#!/bin/bash

source ~/venv/conflictgateway/bin/activate
cd  ~/Projects/conflict-gateway/conflictgateway/scraper/scraper/spiders
scrapy crawl dmejobs
scrapy crawl findaphd
scrapy crawl mediatedotcom
scrapy crawl mediationworld
scrapy crawl sciencedaily
scrapy crawl undotorg
scrapy crawl unjobs
scrapy crawl unpeacejobs
deactivate

