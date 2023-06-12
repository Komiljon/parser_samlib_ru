import requests
import re
from bs4 import BeautifulSoup
import wget
import csv
import numpy as np
import pandas as pd
import os
from os.path import exists

global_url = 'http://samlib.ru'
headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1"
}
output_dir = '/Users/macbook/PycharmProjects/parser_samlib_ru/Data/img'
csv_file = '/Users/macbook/PycharmProjects/parser_samlib_ru/Data/result.csv'

url = 'http://samlib.ru/w/wawulin_n_i/'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
tb = soup.find('table', attrs={'bgcolor': '#e0e0e0'})
email = tb.find('u').text
print(email)
