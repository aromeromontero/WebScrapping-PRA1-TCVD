# Definición de pipelines, para manejar diferentes tipos de artículos con una única interfaz

from itemadapter import ItemAdapter


class SpiderPipeline:
    def process_item(self, item, spider):
        return item
    

# Definición de un pipeline para eliminar espacios en blanco que se presenten en los campos 'production' y 'original_title'
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

