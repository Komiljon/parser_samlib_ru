import requests
import re
from bs4 import BeautifulSoup
import wget
import csv
import numpy as np
import pandas as pd
import os
from os.path import exists

count = 0

global_url = 'http://samlib.ru'
headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1"
}
output_dir = '/Users/macbook/PycharmProjects/parser_samlib_ru/Data/img'
csv_file = '/Users/macbook/PycharmProjects/parser_samlib_ru/Data/url_list.csv'

# Create csv file
with open(csv_file, "w", encoding="utf-8") as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(
        (
            'name',
            'url'
        )
    )

with open('Data/urls.txt', 'r') as urls:
    for url in urls:
        # url = 'http://samlib.ru/b/'
        url = url.rstrip('\n').strip()
        if len(url) <= 0:
            continue
        try:
            response = requests.get(url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'lxml')
                dls = soup.find_all('dl')
                for dl in dls:
                    link = dl.find('a')
                    name = link.text
                    urll = 'http://samlib.ru' + link.get('href')

                    if name is None:
                        name = 'None'
                    if urll is None:
                        urll = 'None'
                    count += 1
                    with open(csv_file, "a", encoding="utf-8") as file:
                        writer = csv.writer(file, delimiter=';')
                        writer.writerow(
                            (
                                name,
                                urll
                            )
                        )
            else:
                print(url + ' --- ' + str(response.status_code))
        except():
            print(url)

print(count)
