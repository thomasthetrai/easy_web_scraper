from bs4 import BeautifulSoup
import requests
import psycopg2
needed = 'https://www.aftonbladet.se'

url = 'https://www.aftonbladet.se/nyheter/a/Rr77qd/aftonbladet-direkt'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'lxml')
bb = soup.find_all('h3', class_='hyperion-css-tn510y')
everything = soup.find_all('span', 'hyperion-css-43tyjz')



try:
    connection = psycopg2.connect(
        host="localhost",
        port="5432",
        user="postgres",
        password="the password you have on the database",
        database="the databse you made"
    )
    
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'lxml')
    time = soup.find_all('span', 'hyperion-css-43tyjz')
    for ggs in time:
        if 'nyheter' in ggs.text.lower():
            timex2 = ggs.find_parent('p', 'hyperion-css-m3gbyz')
            tv1 = timex2.text[0]
            tv2 = timex2.text[1]
            tv3 = timex2.text[2]
            tv4 = timex2.text[3]
            tv5 = timex2.text[4]

        
            timevariabvle = (tv1 + tv2 + tv3 + tv4 + tv5)
            print(timevariabvle)

    cursor = connection.cursor()
    for ggs in everything:
        if 'nyheter' in ggs.text.lower():
            about = ggs.text.lower()
            break

    for bbs in bb:
        klisk = bbs.text
        if 'stockholm' in klisk.lower():
            print(klisk)
            link = bbs.find_parent('a')['href']
            print('link:', link)
            
            insert_query = "INSERT INTO scrapedinfo (about, just_nu_news, link, time) VALUES (%s, %s, %s, %s)"
            data = (about ,klisk, needed + link, timevariabvle)
            print(data)

            cursor.execute(insert_query, data)
            connection.commit()

            print('Data inserted successfully!')
        else:
            if 'sandviken' in klisk.lower():
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
