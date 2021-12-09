import scrapy
from scrapy_splash import SplashRequest
from shopee.items import ShopeeItem
from utils import load_specific_config


class ShopeeSpider(scrapy.Spider):
    name = 'shopee'
    allowed_domains = ['shopee.vn']
    start_urls = load_specific_config('start_urls')
    selectors = load_specific_config('css_selectors')

    render_script = """
        function main(splash)
            local url = splash.args.url
            assert(splash:go(url))
            assert(splash:wait(5))

            return {
                html = splash:html(),
                url = splash:url(),
            }
        end
        """

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(
                url,
                self.parse_pages,
                endpoint='render.html',
                args={
                    'wait': 5,
                    'lua_source': self.render_script,
                }
            )

    def parse_pages(self, response, **kwargs):
        n_pages = int(response.css(self.selectors['n_pages']).extract_first())
        print(n_pages)
        for i in range(n_pages):
            yield SplashRequest(
                url=response.url + f'?page={i}&sortBy=pop',
                callback=self.parse_urls,
                endpoint='render.html',
                args={
                    'wait': 5,
                    'lua_source': self.render_script
                }
            )

    def parse_urls(self, response):
        urls = response.css(
            'div.shop-search-result-view__item.col-xs-2-4 a::attr("href")').getall()

        for url in urls:
            yield SplashRequest(
                url=response.urljoin(url),
                callback=self.parse_detail,
                endpoint='render.html',
                args={
                    'wait': 5,
                    'lua_source': self.render_script
                }
            )

    def parse_detail(self, response, **kwargs):
        item = ShopeeItem()
        
        item['url'] = response.url
        item['shop_name'] = response.css(self.selectors['shop_name']).extract_first()
        item["name"] = response.css(self.selectors['name']).extract_first()
        item["price"] = response.css(self.selectors['price']).extract_first()
        item['discount_rate'] = response.css(self.selectors['rate']).extract_first()
        item['describe'] = response.css(self.selectors['describe']).extract_first()
        item['n_solded'] = response.css(self.selectors['n_solded']).extract_first()

        rating = response.css(self.selectors['rating']).getall()
        rating = rating if rating else [0, 0]
        item['rating_score'], item['n_ratings'] = rating

        item['n_items'] = response.css(self.selectors['n_items']).extract_first()
        item['type'] = ', '.join(response.css(self.selectors['type']).getall())

        yield item
