import scrapy




class SpiderItem(scrapy.Item):
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
