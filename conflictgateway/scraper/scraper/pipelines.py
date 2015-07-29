# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from sqlalchemy.orm import sessionmaker
from models import News, Jobs, db_connect


NEWS_SPIDERS = ["mediationworld", "mediatedotcom", "sciencedaily", "undotorg"]
JOBS_SPIDERS = ["findaphd", "dmejobs", "unjobs", "unpeacejobs"]


class NewsPipeline(object):
     def __init__(self):
        """
        Initializes database connection and sessionmaker.
        """
        engine = db_connect()
        self.Session = sessionmaker(bind=engine)

     def process_item(self, item, spider):
        print "Processing News Pipeline"
        if spider.name in NEWS_SPIDERS:
            """Save news items to the database.

            This method is called for every item pipeline component.

            """
            session = self.Session()
            news = News(**item)

            try:
                if session.query(News).filter(News.title == news.title).count() == 0:
                    session.add(news)
                    session.commit()
            except:
                session.rollback()
                raise
            finally:
                session.close()
        else:
            pass
        return item
        
        
class JobsPipeline(object):
     def __init__(self):
        """
        Initializes database connection and sessionmaker.
        """
        engine = db_connect()
        self.Session = sessionmaker(bind=engine)

     def process_item(self, item, spider):
        print "Processing Jobs Pipeline"
        if spider.name in JOBS_SPIDERS:
            """Save jobs items to the database.

            This method is called for every item pipeline component.

            """
            session = self.Session()
            jobs = Jobs(**item)

            try:
                if session.query(Jobs).filter(Jobs.title == jobs.title).count() == 0:
                    session.add(jobs)
                    session.commit()
            except:
                session.rollback()
                raise
            finally:
                session.close()
        else:
            pass
        return item
