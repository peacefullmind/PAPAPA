import scrapy


class YuqueBookSpider(scrapy.Spider):
    name = 'yuque_book'
    allowed_domains = ['yuque.com']
    start_urls = ['http://yuque.com/']

    def parse(self, response):
        pass
