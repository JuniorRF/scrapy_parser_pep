from pathlib import Path


DOMAIN = 'peps.python.org'

URL = f'https://{DOMAIN}/'

BASE_DIR = Path(__file__).parent.parent

RESULTS = 'results/'

BOT_NAME = 'pep_parse'

SPIDER_MODULES = ['pep_parse.spiders']

ROBOTSTXT_OBEY = True

FEEDS = {
    'results/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True
    },
}

ITEM_PIPELINES = {
    "pep_parse.pipelines.PepParsePipeline": 100,
}
