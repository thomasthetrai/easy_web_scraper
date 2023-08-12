# from urllib.request import urlopen

# url = "http://olympus.realpython.org/profiles/poseidon"
# page = urlopen(url)
# html = page.read().decode("utf-8")
# start_index = html.find("<title>") + len("<title>")
# end_index = html.find("</title>")
# title = html[start_index:end_index]
# print(title)

# import re

# string = "Everything is <replaced> if it's in <tags>. FILLIPHS <colgate>"
# string = re.sub("<.*?>", "INFANTS", string)
# print(string)

# regex_soup.py

# import re
# from urllib.request import urlopen

# url = "http://olympus.realpython.org/profiles/dionysus"
# page = urlopen(url)
# html = page.read().decode("utf-8")

# pattern = "<title.*?>.*?</title.*?>"
# match_results = re.search(pattern, html, re.IGNORECASE)
# title = match_results.group()
# title = re.sub("<.*?>", "", title) # Remove HTML tags

# print(title)
# from bs4 import BeautifulSoup
# from urllib.request import urlopen

# url = "http://olympus.realpython.org/profiles/dionysus"
# page = urlopen(url)
# html = page.read().decode("utf-8")
# soup = BeautifulSoup(html, "html.parser")

# # print(soup)
# import psycopg2
# import requests
# from bs4 import BeautifulSoup


# print("psycopg2 version:", psycopg2.__version__)


# try:
#     connection = psycopg2.connect(
#         host="localhost",
#         port="5432",
#         user="postgres",
#         password="Vallhov16",
#         database="devs"
#     )
#     name_lastname = tuple(input('Enter your first and last name: '))
#     email = tuple(input('Enter your email: '))
#     age = input('Enter your age: ')
#     social_security_code = tuple(input('Enter your socila security cocde: '))
#     info = tuple(name_lastname + email + age + social_security_code)



#     cursor = connection.cursor()
    

#     insert_query = "INSERT INTO devs (name, email, age, social_security_code) VALUES (%s, %s, %s, %s)"



#     dti = [
#         info
#     ]

#     cursor.executemany(insert_query, dti)

#     connection.commit()

#     print('data inserted succesfully!')

# except (Exception, psycopg2.Error) as error:
#     print('error: ', error)

# finally:
#     # Close the cursor and connection
#     if cursor:
#         cursor.close()
#     if connection:
#         connection.close()

#         # Enter
#         # your
#         # first and last
#         # name: Zahra
#         # Hossain
#         # Enter
#         # your
#         # email: zahrahassain4 @ gmail.com
#         # Enter
#         # your
#         # age: 29
#         # Enter
#         # your
#         # socila
#         # security
#         # cocde: 9405030223   
from bs4 import BeautifulSoup
import requests
import psycopg2
needed = 'https://www.aftonbladet.se'

url = 'https://www.aftonbladet.se/nyheter/a/Rr77qd/aftonbladet-direkt'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'lxml')

# Find all the 'a' tags inside the 'main' tag
all_a_tags = soup.find_all('a')
smth2 = None

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


#Loop through all 'a' tags and find the one with 'JUST NU' in the 'aria-label'
# just_nu_news = None
# for a_tag in all_a_tags:
#     aria_label = a_tag.get('aria-label', '').lower()
#     if 'just nu' in aria_label:
#         just_nu_news = a_tag
#         break

# # Extract the 'aria-label' attribute if 'JUST NU' news is found
# if just_nu_news is not None:
#     aria_label = just_nu_news.get('aria-label')
#     print(aria_label)
# else:
#     print("No 'JUST NU' news found.")







