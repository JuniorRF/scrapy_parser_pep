import scrapy

from pep_parse.items import PepParseItem
from pep_parse.settings import URL, DOMAIN


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = [DOMAIN]
    start_urls = [URL]

    def parse(self, response):
        for pep in response.css('.pep').css('a::attr(href)'):
            yield response.follow(pep, callback=self.parse_pep)

    def parse_pep(self, response):
        tag_h1 = response.css('h1.page-title::text').get().split(' – ')
        yield PepParseItem({
            'number': tag_h1[0],
            'name': tag_h1[1],
            'status': response.css('abbr::text').get()
        })
