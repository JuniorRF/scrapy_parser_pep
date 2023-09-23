import csv
import datetime as dt

from pep_parse.settings import BASE_DIR


class PepParsePipeline:
    def __init__(self):
        self.total = 0
        self.statuses = {'Статус': 'Количество'}

    def open_spider(self, spider):
        pass

    def process_item(self, item, spider):
        self.statuses.setdefault(item['status'], 0)
        self.statuses[item['status']] += 1
        self.total += 1
        return item

    def close_spider(self, spider):
        now = dt.datetime.now()
        now_formatted = now.strftime('%Y-%m-%d_%H-%M-%S')
        file_name = f'status_summary_{now_formatted}.csv'
        file_path = BASE_DIR / 'results' / file_name
        with open(file_path, mode='w', encoding='utf-8') as f:
            writer = csv.writer(f, dialect='excel')
            writer.writerows([*self.statuses.items()])
            writer.writerow(['Total', self.total])
