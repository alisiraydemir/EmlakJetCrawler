#Kodu çalıştırmak ve verileri csv dosyasına yazmak için: scrapy crawl -o dosyaadı.csv
#Yukarıdaki kodu yazmadan önce C:\Users\Users_Name\Emlakjet\emlakjet_crawler içerisinde olduğunuzdan emin olun.
#Linki değiştirerek başka semtler için de kullabilirsiniz.
import scrapy
from ..items import EmlakjetCrawlerItem
class EmlakjetSpider(scrapy.Spider):
    name = "emlakjet"

    start_urls = ["https://www.emlakjet.com/satilik-konut/ankara-cankaya/{}".format(i) for i in range(1, 3)]


    def parse(self, response):
        linkler = response.xpath("//div[@class='ej64 ej100 ej156 _2g-Ygo']//a[starts-with(@href, '/ilan')]/@href").getall()
        for link in linkler:
            absolute_url = response.urljoin(link)
            yield scrapy.Request(absolute_url, callback=self.parse_listing)

    def parse_listing(self, response):
        item = EmlakjetCrawlerItem()

        item['brut_metrekare'] = response.xpath(
            "//div[@class='_1bVOdb' and text()='Brüt Metrekare']/following-sibling::*/text()").get()
        item['oda_sayisi'] = response.xpath(
            "//div[@class='_1bVOdb' and text()='Oda Sayısı']/following-sibling::*/text()").get()
        item['binanin_yasi'] = response.xpath(
            "//div[@class='_1bVOdb' and text()='Binanın Yaşı']/following-sibling::*/text()").get()
        item['bina_kat_sayisi'] = response.xpath(
            "//div[@class='_1bVOdb' and text()='Binanın Kat Sayısı']/following-sibling::*/text()").get()
        item['kullanim_durumu'] = response.xpath(
            "//div[@class='_1bVOdb' and text()='Kullanım Durumu']/following-sibling::*/text()").get()
        item['krediye_uygunluk'] = response.xpath(
            "//div[@class='_1bVOdb' and text()='Krediye Uygunluk']/following-sibling::*/text()").get()
        if item['krediye_uygunluk'] is None:
            item['krediye_uygunluk'] = response.xpath("//div[@class='_1YVE8i']//text()").get()
        item['kira_getirisi'] = response.xpath(
            "//div[@class='_1bVOdb' and text()='Kira Getirisi']/following-sibling::*/text()").get()
        item['esya_durumu'] = response.xpath(
            "//div[@class='_1bVOdb' and text()='Eşya Durumu']/following-sibling::*/text()").get()
        item['fiyat_bilgisi'] = response.xpath(
            '//*[@id="__next"]/div[3]/div[2]/div[1]/div[1]/div[2]/div[2]/text()').get()
        item['ilan_link'] = response.request.url


        yield item


