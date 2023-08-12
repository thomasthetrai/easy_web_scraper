 from bs4 import BeautifulSoup
import requests
import psycopg2
needed = 'https://www.aftonbladet.se'

url = 'https://www.aftonbladet.se/nyheter/a/Rr77qd/aftonbladet-direkt'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'lxml')


bb = soup.find_all('h3', class_='hyperion-css-tn510y')

try:
    connection = psycopg2.connect(
        host="localhost",
        port="5432",
        user="postgres",
        password="Vallhov16",
        database="scraped"
    )

    cursor = connection.cursor()

    for bbs in bb:
        klisk = bbs.text
        if 'ryssland' in klisk.lower():
            print(klisk)
            link = bbs.find_parent('a')['href']
            print('link:', link)
            
            insert_query = "INSERT INTO scrapedinfo (just_nu_news, link) VALUES (%s, %s)"
            data = (klisk, needed + link)

            cursor.execute(insert_query, data)
            connection.commit()

            print('Data inserted successfully!')
        else:
            if 'ukraina' in klisk.lower():
                print(klisk)
                link = bbs.find_parent('a')['href']
                print('link:', link)
                
                insert_query = "INSERT INTO scrapedinfo (just_nu_news, link) VALUES (%s, %s)"
                data = (klisk, needed + link)

                cursor.execute(insert_query, data)
                connection.commit()

                print('Data stored')



finally:
    if cursor:
        cursor.close()
    if connection:
        connection.close()









