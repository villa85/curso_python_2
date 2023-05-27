import scrapy


class AmazonLibrosSpider(scrapy.Spider):
    name = "amazon_libros"
    allowed_domains = ["www.amazon.es"]
    start_urls = ["https://www.amazon.es/gp/bestsellers/books"]

    def parse(self, response):
        print("procesando:", response.url)

        # Extraemos los datos usando selectores css

        nombres = response.xpath('//a[@class="a-link-normal"]/span/div/text()').extract()
        autores = response.xpath('//span[@class="a-size-small a-color-base"]/div/text()').extract()
        precios = response.css(".p13n-sc-price::text").extract()
        valoracion = response.css(".a-icon-alt::text").extract()

        # Normalizamos los datos

        for item in zip(nombres, autores, precios, valoracion):
            scraped_info = {
            'pagina': response.url,
            'libros': item[0],
            'autores': item[1],
            'precio': item[2],
            'valoracion':item[3]
            }
            print(scraped_info)
            yield scraped_info

        NEXT_PAGE_SELECTOR = 'ul.a-pagination > li.a-last > a::attr(href)'
        next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
        if next_page:
            yield scrapy.Request(response.urljoin(next_page), callback=self.parse)
