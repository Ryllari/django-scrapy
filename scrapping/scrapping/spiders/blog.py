import scrapy

from app.models import BlogPost
from scrapping.items import BlogPostItem
from scrapy.linkextractors import LinkExtractor
from scrapy.contrib.spiders import Rule

class WattPanelSpider(scrapy.Spider):
    """
    This class define a Spider that scrapes posts from WattPanel blog
    """
    name = "wattpanel"
    allowed_domains = ["blog.wattpanel.com.br"]
    start_urls = (
        "http://blog.wattpanel.com.br/",
    )

    Rules = (
        Rule(
            LinkExtractor(
            allow=(), 
            restrict_xpaths=('//a[@class="next page-numbers"]',)
            ),
        callback="parse",
        follow= True
        ),
    )

    def parse(self, response):
        for idx, article in enumerate(response.xpath('//article')):
            item = BlogPostItem()
            title = article.xpath('.//h3/a/text()').extract_first()
            item['title'] = title
            item['posted_at'] = article.xpath(
                './/time[@class="entry-date published"]/@datetime'
                ).extract_first()
            text_xpath = './/div[@class="entry-content"]/p/text()'
            item['short_text'] = ''.join(
                [text for text in article.xpath(text_xpath).extract()]
            )
            
            yield item
        
        # Verify if contains more pages
        next_page = response.xpath('//a[@class="next page-numbers"]/@href').extract_first()
        if next_page:
            request = scrapy.Request(url=next_page)
            yield request