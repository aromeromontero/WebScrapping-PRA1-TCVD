# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

from itemloaders.processors import MapCompose



class SpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = Field()
    title = scrapy.Field()
    original_title = scrapy.Field()
    release_year = scrapy.Field()
    country = scrapy.Field()
    directors = scrapy.Field()
    cast = scrapy.Field()
    genre = scrapy.Field()
    production = scrapy.Field()
    sinopsis = scrapy.Field()
    rating = scrapy.Field()
