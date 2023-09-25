import scrapy

from pep_parse.items import PepParseItem
from pep_parse.settings import URL


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = [URL]
    start_urls = ['https://' + URL]

    def parse(self, response):
        for pep in response.css('.pep').css('a::attr(href)'):
            yield response.follow(pep, callback=self.parse_pep)

    def parse_pep(self, response):
        name = response.css('h1.page-title::text').get()
        number_pep = name.split()[1],
        yield PepParseItem({
            'number': number_pep,
            'name': name,
            'status': response.css('abbr::text').get()
        })
