from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class CrawlingBug(CrawlSpider):
    name = "happycrawler"

    # list of scraping domains
    allowed_domains = ["toscrape.com"]

    # base point (where we start scraping from)
    start_urls = ["http://books.toscrape.com/"]

    rules = (
        Rule(LinkExtractor(allow="catalogue/category")),
    )
