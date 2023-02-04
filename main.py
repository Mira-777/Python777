import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

gdz = "https://gdz.ru"
r = requests.get(gdz)
print(r.status_code)