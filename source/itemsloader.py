from itemloaders.processors import MapCompose
from scrapy.loader import ItemLoader
from w3lib.html import replace_escape_chars

punctuation = '''!-[]{};:'"\,<>./?@#$%^&*_~'''

class SpiderItemLoader(ItemLoader):
    title_in = MapCompose(lambda v: v.strip(), replace_escape_chars)
    original_title_in = MapCompose(lambda v: v.strip(), replace_escape_chars)
    rating_in = MapCompose(lambda v: v.strip(), replace_escape_chars)
    production_in = MapCompose(lambda v: v.strip(punctuation))
