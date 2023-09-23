import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        for pep in response.css('.pep').css('a::attr(href)'):
            yield response.follow(pep, callback=self.parse_pep)

    def parse_pep(self, response):
        yield PepParseItem({
            'number': response.css('h1.page-title::text').get().split()[1],
            'name': response.css('h1.page-title::text').get(),
            'status': response.css('abbr::text').get()
        })
