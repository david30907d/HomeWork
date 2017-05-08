# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
import requests
import shutil

class ZmtiantangSpider(scrapy.Spider):
    name = "zmtiantang"
    allowed_domains = ["www.zmtiantang.com"]
    start_urls = list(map(lambda x:'http://www.zmtiantang.com/e/action/ListInfo/?classid=1&page=' + str(x), range(0, 5630)))

    def parse(self, response):
        res = BeautifulSoup(response.body)
        downloadURL = res.select('span.label-danger')
        for i in downloadURL:
            yield scrapy.Request('http://'+self.allowed_domains[0] + i.parent['href'], callback=self.parse_detail)

    def parse_detail(self, response):
        res = BeautifulSoup(response.body)
        download = res.select('.btn-sm')[0]
        self.download_file('http://'+self.allowed_domains[0] + download['href'])

    @staticmethod
    def download_file(url):
        local_filename = url.split('/')[-1]
        r = requests.get(url, stream=True)
        with open(local_filename + '.zip', 'wb') as f:
            shutil.copyfileobj(r.raw, f)