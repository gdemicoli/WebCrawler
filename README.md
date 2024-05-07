Important Scrapy Terminal Functions:

    scrapy shell my.url.com
        opens scrapy & crawls webpage, can be used interactively.
        You are given response object and can use to retrive data 
        based on how its type in css.
        e.g. response.css("h1")
        Will retrieve all the heading 1 elements