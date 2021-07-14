import scrapy


import logging
logger = logging.getLogger(__name__)


class Spider1Spider(scrapy.Spider):
    name = 'spider1'
    allowed_domains = ['itcast.com']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml#aweb']
    # start_url要根据需求改变，一般不会直接使用默认提供的

    def parse(self, response):


        # start url的响应
        get = response.xpath("//div[@class='tea_con']//li//div")
        # print(get.extract())
        # extract 将结果中的文字以list提取

        for x in get:

            name = x.xpath('.//h3/text()').extract_first()
            # 直接抓第一个，没有就none

            title = x.xpath('.//h4/text()').extract_first()
            intro = x.xpath('.//p/text()').extract_first().strip()
            item = {}
            item['name'] = name
            item['title'] = title
            item['intro'] = intro

            # logger.warning(item)

            # 以log的warning形式输出
            # 由于log_level设置为warning，因此低于warning的信息不显示
            # 可以显示输出时间、来源

            yield item
            # 在此yield 由pipelines接受
            # item必须是响应对象/dict/none

