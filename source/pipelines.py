# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class SpiderPipeline:
    def process_item(self, item, spider):
        return item

class RemoveBlankSpacesPipeline:

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        if adapter.get('production'):

            test_list = [i for i in adapter['production'] if i != ' ' if i != '']

            adapter['production'] = test_list

            return item

        if adapter.get('original_title'):

            test_list = [i for i in adapter['original_title'] if i != ' ' if i != '']

            adapter['original_title'] = test_list

            return item

