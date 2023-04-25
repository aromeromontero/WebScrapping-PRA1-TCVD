# Definición del item, a partir del cual se estructurarán los datos extraídos

import scrapy

from itemloaders.processors import MapCompose



class SpiderItem(scrapy.Item):
    # Definición de los campos para el item, en formato clave-valor
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
