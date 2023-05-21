import scrapy


class AmazonTabletasSpider(scrapy.Spider):
    name = "amazon_tabletas"
    allowed_domains = ["www.amazon.es"]
    start_urls = ["https://www.amazon.es/gp/bestsellers/computers/938010031/"]

    def parse(self, response):
        print("procesando:", response.url)

        # Extraemos los datos usando selectores css
        nombres = response.css("._cDEzb_p13n-sc-css-line-clamp-3_g3dy1::text").extract()
        precios = response.xpath("//span[@class='p13n-sc-price']/text()").extract()

        # Normalizamos los datos

        for item in zip(nombres, precios):
            scraped_info = {
                'pagina': "Amazon",
                'tableta': item[0],
                'precio': item[1][:-2]
            }
            yield scraped_info

        NEXT_PAGE_SELECTOR = 'ul.a-pagination > li.a-last > a::attr(href)'
        next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
        if next_page:
            yield scrapy.Request(response.urljoin(next_page), callback=self.parse)