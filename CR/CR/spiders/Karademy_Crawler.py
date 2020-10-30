import scrapy


class LinkCheckerSpider(scrapy.Spider):
    name = 'link_checker'
    start_urls = ['https://video.varzesh3.com/']

    def parse(self, response):
        """parse the downloaded pages"""

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
