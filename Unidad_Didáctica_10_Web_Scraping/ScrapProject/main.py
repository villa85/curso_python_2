from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import os

import pandas as pd

os.chdir(r"C:\\Users\\villa\\curso_python\\curso_python_2\\Unidad_Didáctica_10_Web_Scraping\\ScrapProject\\amazonlibros\\amazonlibros\\spiders")


process = CrawlerProcess(get_project_settings())

process.crawl('amazon_libros')
process.start() # the script will block here until the crawling is finished

df = pd.read_csv("amazonlibros.csv", encoding = "utf-8")
print(df)
