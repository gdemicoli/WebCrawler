Important Scrapy Terminal Functions:

    scrapy shell my.url.com
        opens scrapy & crawls webpage, can be used interactively.
        You are given response object and can use to retrive data 
        based on how its type in css.
        e.g. response.css("h1")
        Will retrieve all the heading 1 elements
        
        response.get() retrieves actual HTML code
        response.css("h1::text").get() retrieves only the text
        NOTE: .get() will only retrieve one element
            so use .getall() to retrieve all 

        response.xpath().extract

    To place results in json file:
        In terminal: scrapy crawl happycrawler -o output.json
