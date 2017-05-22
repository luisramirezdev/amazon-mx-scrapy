import sys
reload(sys)
sys.setdefaultencoding('utf8')

import scrapy
from scrapy.spider import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import CloseSpider
from amazon.items import AmazonItem

class AmazonSpider(CrawlSpider):
	name = 'amazon'
	item_count = 0
	allowed_domain = ['www.amazon.com.mx']
	start_urls = ['https://www.amazon.com.mx/s/ref=sr_nr_n_1?fst=as%3Aoff&rh=n%3A9725870011%2Ck%3Ahornos+microondas&keywords=hornos+microondas&ie=UTF8&qid=1489902581&rnid=15997893011']

	rules = {
		Rule(LinkExtractor(allow = (), restrict_xpaths = ('//span[@class="pagnRA"]'))),
		Rule(LinkExtractor(allow = (), restrict_xpaths = ('//*[contains(@class, "a-link-normal s-access-detail-page")]')),
							callback = 'parse_item', follow = False)
	}


	def parse_item(self, response):
		a_item = AmazonItem()
		#informacion general
		a_item['nombre'] = response.xpath('normalize-space(//span[@id="productTitle"]/text())').extract()
		a_item['precio'] = response.xpath('normalize-space(//span[@id="priceblock_ourprice"]/text())').extract()
		a_item['precio_recomendado'] = response.xpath('normalize-space(//span[@class="a-text-strike"]/text())').extract()
		a_item['ahorro'] = response.xpath('normalize-space(//td[contains(@class, "a-span12 a-color-price a-size-base")]/text())').extract()
		a_item['envio'] = response.xpath('normalize-space(//span[@id="price-shipping-message"]/b/text())').extract()
		a_item['descripcion_corta'] = response.xpath('normalize-space(//div[@id="feature-bullets"]/ul/li/span').extract()
		a_item['vendido_por'] = response.xpath('normalize-space(//a[@id="brand"]/text())').extract()
		#informacion tecnica
		a_item['marca'] = response.xpath('normalize-space(//*[@id="detail_bullets_id"]/table/tbody/tr/td/div[2]/ul/li[1]/text())').extract()
		a_item['modelo'] = response.xpath('normalize-space(//*[@id="detail_bullets_id"]/table/tbody/tr/td/div[2]/ul/li[2]/text())').extract()
		a_item['modelo_ano'] = response.xpath('normalize-space(//*[@id="detail_bullets_id"]/table/tbody/tr/td/div[2]/ul/li[2]/text())').extract()
		a_item['num_parte'] = response.xpath('normalize-space(//*[@id="detail_bullets_id"]/table/tbody/tr/td/div[2]/ul/li[2]/text())').extract()
		a_item['caracteristicas_esp'] = response.xpath('normalize-space(//*[@id="detail_bullets_id"]/table/tbody/tr/td/div[2]/ul/li[2]/text())').extract()
		a_item['tamano_pantalla'] = response.xpath('normalize-space(//*[@id="detail_bullets_id"]/table/tbody/tr/td/div[2]/ul/li[2]/text())').extract()
		a_item['tipo_pantalla'] = response.xpath('normalize-space(//*[@id="detail_bullets_id"]/table/tbody/tr/td/div[2]/ul/li[2]/text())').extract()
		#informacion adicional
		a_item['peso'] = response.xpath('normalize-space(//*[@id="detail_bullets_id"]/table/tbody/tr/td/div[2]/ul/li[6]/text())').extract()
		a_item['peso_envio'] = response.xpath('normalize-space(//*[@id="detail_bullets_id"]/table/tbody/tr/td/div[2]/ul/li[6]/text())').extract()
		a_item['num_modelo'] = response.xpath('normalize-space(//*[@id="detail_bullets_id"]/table/tbody/tr/td/div[2]/ul/li[6]/text())').extract()
		a_item['asin'] = response.xpath('normalize-space(//*[@id="prodDetails"]/div/div[2]/div/div[2]/div/div/table/tbody/tr[4]/td[2]/text())').extract()
		a_item['producto_amazon_desde'] = response.xpath('normalize-space(//*[@id="detail_bullets_id"]/table/tbody/tr/td/div[2]/ul/li[6]/text())').extract()
		a_item['opinion_media'] = response.xpath('normalize-space(//div[@id="avgRating"]/span/text())').extract()

		#imagenes
		a_item['image_urls'] = response.xpath('//*[@id="landingImage"]/@src').extract()
		a_item['image_name'] = response.xpath('normalize-space(//span[@id="productTitle"]/text())').extract_first()

		self.item_count += 1
		if self.item_count > 10:
			raise CloseSpider('item_exceeded')
		yield a_item 

