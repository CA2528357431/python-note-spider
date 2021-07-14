import scrapy


class Page1Spider(scrapy.Spider):
    name = 'page1'
    allowed_domains = ['cn.bing.com']
    start_urls = ['https://cn.bing.com/search?q=你好']

    def parse(self, response):

        get = response.xpath("/html/body/div/main/ol/li[@class='b_algo']")

        for x in get:
            title_or = x.xpath("./div/h2/a")
            title = x.xpath("string(.)").extract_first()
            print(title)
            print()
