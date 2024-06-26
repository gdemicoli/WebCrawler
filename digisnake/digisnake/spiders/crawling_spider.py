from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class CrawlingBug(CrawlSpider):
    name = "happycrawler"

    PROXY_SERVER = "myIP address"

    # list of scraping domains
    allowed_domains = ["toscrape.com"]

    # base point (where we start scraping from)
    start_urls = ["http://books.toscrape.com/"]

    rules = (
        Rule(LinkExtractor(allow="catalogue/category")),
        Rule(LinkExtractor(allow="catalogue", deny="category"), callback="parse_item"),
    )

    def parse_item(self, response):
        yield {

            # This will get the title & the price based on their data types in css
            "title": response.css(".product_main h1::text").get(),
            "price": response.css(".price_color::text").get(),
            # we use the [1] because we are going to be returned 1 parts of the data
            # we only want the 2nd one (use regex if you only want the numerical value)
            "availability": response.css(".availability::text")[1].get().replace("\n", "").replace(" ",""),

        }
