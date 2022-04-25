import scrapy


class LinkCheckerSpider(scrapy.Spider):
    """sends requests from the start_urls spider attribute and 
    calls the spider’s method parse for each of the resulting responses.
    """

    name = 'link_checker'
    start_urls = ['https://video.varzesh3.com/']

    def parse(self, response):
        """parse the downloaded pages.

        Args:
        response: the response to parse
        
        Returns:
        An iterable of request
        """
        # Get all the <a> tags
        a_selectors = response.xpath("//a")
        # Loop on each tag
        for selector in a_selectors:
            yield {
                # Extract the link text
                'text': selector.xpath("text()").extract_first(),
                # Extract the link href
                'link': selector.xpath("@href").extract_first(),
            }

# scrapy crawl link_checker
# scrapy crawl link_checker -o link_checker.csv
