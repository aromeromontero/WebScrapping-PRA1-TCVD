import random
import scrapy

from ..items import SpiderItem
from ..itemsloader import SpiderItemLoader
from scrapy_selenium import SeleniumRequest


# Definir lista de agentes de usuario
user_agent_list = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
    'AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) '
    'AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1; Win64; x64) '
    'AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2; Win64; x64) '
    'AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) '
    'AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/44.0.2403.157 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) '
    'AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
    'AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) '
    'AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
    'AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/55.0.2883.87 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) '
    'AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/55.0.2883.87 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) '
    'AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/53.0.2785.116 Safari/537.36'
    'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 6.2; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; '
    'Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)',
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:59.0) Gecko/20100101 Firefox/59.0'
]

# Función que devuelve un agente usuario aleatorio de la lista
def get_random_agent():
    return random.choice(user_agent_list)


# Definimos la clase FilmSpider
class FilmspiderSpider(scrapy.Spider):
    name = "filmspider"     # Asignamos el nombre con el que llamaremos al scrapy crawl

    allowed_domains = ["filmaffinity.com/es"]   # Asignamos el atributo allowed_domains

    start_urls = ["https://www.filmaffinity.com/es/ranking.php?rn=ranking_fa_movies"]   # Asignamos la url que contiene el ranking

    # TODO: Scroll down: si no se puede, hay que eliminar el chrome

# Definimos la función de devolución de llamada que se llevará a cabo cuando la araña realice una solicitud a la url de inicio
    def parse(self, response, **kwargs):

        print("Inicio")

        movie_links = response.xpath("//div[@class='mc-title']/a/@href").extract()  # recorre todos los links de la página de los que se extraerán los items

        print("Longitud de lista de películas:", len(movie_links))

# Realizamos un SeleniumRequest a la URl de inicio escogiendo un user-agent random
        for link in movie_links:
            yield SeleniumRequest(url=link,
                                  headers={"User-Agent": get_random_agent()},
                                  dont_filter=True,
                                  callback=self.parseitem
                                  )

# Función que cree un objeto SpiderItemLoader que extraiga los datos de la página y los cargue en un objeto SpiderItem
    def parseitem(self, response):

        movie = SpiderItemLoader(item=SpiderItem(), response=response)
        movie.add_xpath('title', "//h1[@id='main-title']/span[@itemprop='name']/text()")
        movie.add_xpath('original_title', "//dl[@class='movie-info']/dd[1]/text()")
        movie.add_xpath('release_year', "//dl//dd[@itemprop='datePublished']/text()")
        movie.add_xpath('country', "//dl//dd//span[@id='country-img']/img[@class='nflag']/@alt")
        movie.add_xpath('directors', "//dl//span[@itemprop='director']/a/@title")
        movie.add_xpath('cast', "//dl//dd[@class='card-cast']//span[@itemprop='name']/text()")
        movie.add_xpath('genre', "//dl//dd[@class='card-genres']//a/text()")
        movie.add_xpath('production', "//dd[@class='card-producer']//span/text()")
        movie.add_xpath('sinopsis', "//dl//dd[@itemprop='description']/text()")
        movie.add_xpath('rating', "//div[@itemprop='ratingValue']/text()")

        yield movie.load_item()

# Para ejecutar la araña, hay que asegurarse de estar en el directorio de spider de
# la terminal y poner scrapy crawl filmspider
