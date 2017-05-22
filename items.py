# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonItem(scrapy.Item):

    #informacion general
    nombre = scrapy.Field()
    precio_recomendado = scrapy.Field()
    precio = scrapy.Field()
    ahorro = scrapy.Field()
    envio = scrapy.Field()
    descripcion_corta = scrapy.Field()
    vendido_por = scrapy.Field()
    informacion tecnica
    marca = scrapy.Field()
    modelo = scrapy.Field()
    modelo_ano = scrapy.Field()
    num_parte = scrapy.Field()
    caracteristicas_esp = scrapy.Field()
    tamano_pantalla = scrapy.Field()
    tipo_pantalla = scrapy.Field()
    informacion adicional
    peso = scrapy.Field()
    peso_envio = scrapy.Field()
    num_modelo = scrapy.Field()
    asin = scrapy.Field()
    producto_amazon_desde = scrapy.Field()
    opinion_media = scrapy.Field()

    #imagenes
    image_urls = scrapy.Field()
    images = scrapy.Field()
    image_name = scrapy.Field()
