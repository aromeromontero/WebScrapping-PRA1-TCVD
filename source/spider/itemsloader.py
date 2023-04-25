# Definición del itemloader, es decir, el mecanismo mediante el cual poblar los ítems. 

from itemloaders.processors import MapCompose
from scrapy.loader import ItemLoader
from w3lib.html import replace_escape_chars

punctuation = '''!-[]{};:'"\,<>./?@#$%^&*_~'''

class SpiderItemLoader(ItemLoader):
    # Declaración de procesos de input: para título, título original y rating, se reemplazarán los caracteres de escape. 
    title_in = MapCompose(lambda v: v.strip(), replace_escape_chars)
    original_title_in = MapCompose(lambda v: v.strip(), replace_escape_chars)
    rating_in = MapCompose(lambda v: v.strip(), replace_escape_chars)
    # En production, se eliminarán los signos de puntuación definidos en la línea 7
    production_in = MapCompose(lambda v: v.strip(punctuation))
