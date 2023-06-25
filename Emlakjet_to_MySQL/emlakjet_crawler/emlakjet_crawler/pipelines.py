import mysql.connector

class EmlakjetCrawlerPipeline(object):
    def __init__(self):
        self.create_connection()  # Create a database connection
        self.create_table()  # Create the 'emlak' table in the database

    def create_connection(self):
        # Establish a connection to the MySQL database
        self.connection = mysql.connector.connect(
            host='host_adress',
            user='user_name',
            password='password',
            database='database_name'
        )
        self.cursor = self.connection.cursor()

    def create_table(self):
        create_table_query = '''
        CREATE TABLE IF NOT EXISTS emlak (
            id INT AUTO_INCREMENT PRIMARY KEY,
            brut_metrekare VARCHAR(255),
            oda_sayisi VARCHAR(255),
            binanin_yasi VARCHAR(255),
            bina_kat_sayisi VARCHAR(255),
            kullanim_durumu VARCHAR(255),
            krediye_uygunluk VARCHAR(255),
            kira_getirisi VARCHAR(255),
            esya_durumu VARCHAR(255),
            fiyat_bilgisi VARCHAR(255),
            ilan_link VARCHAR(255)
        )
        '''
        self.cursor.execute(create_table_query)  # Execute the query to create the table
        self.connection.commit()

    def process_item(self, item, spiders):
        insert_query = '''
        INSERT INTO emlak (
            brut_metrekare, oda_sayisi, binanin_yasi, bina_kat_sayisi,
            kullanim_durumu, krediye_uygunluk, kira_getirisi, esya_durumu,
            fiyat_bilgisi, ilan_link
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        '''

        data = (
            item['brut_metrekare'],
            item['oda_sayisi'],
            item['binanin_yasi'],
            item['bina_kat_sayisi'],
            item['kullanim_durumu'],
            item['krediye_uygunluk'],
            item['kira_getirisi'],
            item['esya_durumu'],
            item['fiyat_bilgisi'],
            item['ilan_link']
        )

        self.cursor.execute(insert_query, data)  # Execute the insert query with the data
        self.connection.commit()  # Commit the changes to the database
