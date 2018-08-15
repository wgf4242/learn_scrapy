# scrapy runspider filename.py -s LOG_ENABLED=False
import scrapy


class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    # start_urls = ['https://www.0daydown.com/08/910600.html', ]
    start_urls = [line.rstrip('\n') for line in open('urls.txt')]

    def parse(self, response):
        for title in response.css('.article-title>a'):
            yield {'title': title.css('a ::text').extract_first()}
            yield print("{}\n{}".format(title.css('a ::text').extract_first(), response.url))

        # for next_page in response.css('div.prev-post > a'):
        #     yield response.follow(next_page, self.parse)
