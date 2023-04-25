# Configuraciones de scrapy para el proyecto


BOT_NAME = "spider"

SPIDER_MODULES = ["spider"]
NEWSPIDER_MODULE = "spider"


# Se le indica que debe obedecer las instrucciones del fichero robots.txt
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 10

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16


# Activación de Middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    "spider.middlewares.SpiderDownloaderMiddleware": 543,
    "scrapy_selenium.SeleniumMiddleware": 800
}


# Activación de pipelines
ITEM_PIPELINES = {
    "spider.pipelines.SpiderPipeline": 300,
    "spider.pipelines.RemoveBlankSpacesPipeline": 300,
}

# Configuración por defecto: Se establecen configuraciones cuyo valor predeterminado esté en desuso a un valor a prueba de futuro
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"

# Se indica que el output se debe guardar en un fichero csv, y que debe sobreescribir en caso de una nueva petición

FEEDS = {
    'data.csv': {'format': 'csv', 'overwrite': True}
}

# for Chrome Driver (PENDIENTE)

from shutil import which

SELENIUM_DRIVER_NAME = 'chrome'
SELENIUM_DRIVER_EXECUTABLE_PATH = which('chromedriver')
SELENIUM_DRIVER_ARGUMENTS=['--headless']

