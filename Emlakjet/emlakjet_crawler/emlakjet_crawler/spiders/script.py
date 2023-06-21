#Kodu çalıştırmak ve verileri csv dosyasına yazmak için: scrapy crawl -o dosyaadı.csv
#Yukarıdaki kodu yazmadan önce C:\Users\Users_Name\Emlakjet\emlakjet_crawler içerisinde olduğunuzdan emin olun.
#Linki değiştirerek başka semtler için de kullabilirsiniz.
import scrapy
class EmlakjetSpider(scrapy.Spider):
    name = "emlakjet"

    start_urls = ["https://www.emlakjet.com/satilik-konut/ankara-cankaya/{}".format(i) for i in range(1, 10)]


    def parse(self, response):
        linkler = response.xpath("//div[@class='ej64 ej100 ej156 _2g-Ygo']//a[starts-with(@href, '/ilan')]/@href").getall()
        for link in linkler:
            absolute_url = response.urljoin(link)
            yield scrapy.Request(absolute_url, callback=self.parse_listing)

    def parse_listing(self, response):
        metrekare_deger = response.xpath("//div[@class='_1bVOdb' and text()='Brüt Metrekare']/following-sibling::*/text()").get()
        oda_sayisi = response.xpath("//div[@class='_1bVOdb' and text()='Oda Sayısı']/following-sibling::*/text()").get()
        bina_yas = response.xpath("//div[@class='_1bVOdb' and text()='Binanın Yaşı']/following-sibling::*/text()").get()
        bina_kat_sayisi = response.xpath("//div[@class='_1bVOdb' and text()='Binanın Kat Sayısı']/following-sibling::*/text()").get()
        kullanim_durumu = response.xpath("//div[@class='_1bVOdb' and text()='Kullanım Durumu']/following-sibling::*/text()").get()
        krediye_uygunluk = response.xpath("//span[@class='GglL5e']/text()").get()
        kira_getirisi = response.xpath("//div[@class='_1bVOdb' and text()='Kira Getirisi']/following-sibling::*/text()").get()
        esya_durumu = response.xpath("//div[@class='_1bVOdb' and text()='Eşya Durumu']/following-sibling::*/text()").get()
        fiyat_bilgisi = response.xpath('//*[@id="__next"]/div[3]/div[2]/div[1]/div[1]/div[2]/div[2]/text()').get()
        ilan_link = response.request.url

        data = {
            'Brüt Metrekare': metrekare_deger,
            'Oda Sayısı': oda_sayisi,
            'Binanın Yaşı': bina_yas,
            'Bina Kat Sayısı': bina_kat_sayisi,
            'Kullanım Durumu': kullanim_durumu,
            'Krediye Uygunluk': krediye_uygunluk,
            'Kira Getirisi': kira_getirisi,
            'Eşya Durumu': esya_durumu,
            'Fiyat Bilgisi': fiyat_bilgisi,
            'İlan Link': ilan_link,
        }

        yield data
