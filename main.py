import requests
from bs4 import BeautifulSoup
import csv
import numpy as np
import pandas as pd
import time

ok_count = 0
er_count = 0

global_url = 'http://samlib.ru'
output_dir = 'Data/img'
csv_file = 'Data/url_list.csv'
emails_data_csv = 'Data/result_list.csv'
error_data_csv = 'Data/error_list.csv'

def getEmail(url):
    headers = {
        "Accept": "*/*",
        "User-Agent": "Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1"
    }
    try:
        email = 'None'
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'lxml')
            tb = soup.find('table', attrs={'bgcolor': '#e0e0e0'})
            if tb is not None:
                tb_u = tb.find('u')
                if tb_u is not None:
                    email = tb_u.text
        else:
            email = 'error'
    except():
        email = 'None'
    return email


# Create csv file
with open(emails_data_csv, "w", encoding="utf-8") as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(
        (
            'name',
            'url',
            'email'
        )
    )

# Create csv file
with open(error_data_csv, "w", encoding="utf-8") as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(
        (
            'name',
            'url',
            'email'
        )
    )

#Получаем url  url_list.csv
article_read = pd.read_csv(csv_file, delimiter=';')
result = article_read[['name', 'url']]
counts = article_read.url.count()

#Начинаем парсить полученные адреса
for i in range(counts):
    name = result['name'][i]
    url = result['url'][i]
    resEmail = getEmail(url)
    if resEmail == 'None' or resEmail == 'error':
        with open(error_data_csv, "a", encoding="utf-8") as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(
                (
                    name,
                    url,
                    resEmail
                )
            )
        er_count += 1
    else:
        with open(emails_data_csv, "a", encoding="utf-8") as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(
                (
                    name,
                    url,
                    resEmail
                )
            )
        ok_count += 1
    if i >= 5000:
        time.sleep(3)

print('success: ' + str(ok_count))
print('errors: ' + str(er_count))