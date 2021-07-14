# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class DespiderPipeline:
    def process_item(self, item, spider):
        # 此时接受的pipe是 spider/上一个pipe传送的数据流

        if spider.name == 'spider1':
        # 数据流的来源spider
        # 因为所有spider的数据流都会经过pipe

            del item['intro']

        return item
        # 此时返回的return是下一个pipe接受的item

import logging
logger = logging.getLogger(__name__)


class DespiderPipeline1:
    def process_item(self, item, spider):

        logger.warning(item)
        print(item)

        return item

