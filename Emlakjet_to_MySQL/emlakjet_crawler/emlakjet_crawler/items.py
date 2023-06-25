# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class EmlakjetCrawlerItem(scrapy.Item):
    brut_metrekare = scrapy.Field()
    oda_sayisi = scrapy.Field()
    binanin_yasi = scrapy.Field()
    bina_kat_sayisi = scrapy.Field()
    kullanim_durumu = scrapy.Field()
    krediye_uygunluk = scrapy.Field()
    kira_getirisi = scrapy.Field()
    esya_durumu = scrapy.Field()
    fiyat_bilgisi = scrapy.Field()
    ilan_link = scrapy.Field()
