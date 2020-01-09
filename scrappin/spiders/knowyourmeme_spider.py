import scrapy


class KnowYourMemeSpider(scrapy.Spider):
    name = 'knowyourmeme'
    start_urls = ['https://knowyourmeme.com']

    def start_requests(self):
        yield scrapy.Request(
            'https://knowyourmeme.com/memes/page/1'
        )
        
    def parse(self, response):
        # Select fixed 200px width images
        image_urls = response.xpath('//a[@class="photo"]//img/@data-src').extract()
        yield {
            'image_urls': response.xpath('//a[@class="photo"]//img/@data-src').extract()
        }
        
        next_href = response.xpath(
            "//a[@class='next_page']/@href").extract_first()
        if next_href:
            yield scrapy.Request(response.urljoin(next_href))
