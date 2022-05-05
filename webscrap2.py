from bs4 import BeautifulSoup
# import time
import csv
import requests
import pandas as pd

#creating a variable for our URL
URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

#requesting data
r = requests.get(URL)
soup = BeautifulSoup(r.text,'html.parser')

table = soup.find_all('table')
temp = []
rows = table[4].find_all('tr')
for tr in rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp.append(row)
n = []
d = []
m = []
r = []
for i in range(1,len(temp))   :
    n.append(temp[i][0])
    m.append(temp[i][5])
    d.append(temp[i][7])
    r.append(temp[i][8])     
df = pd.DataFrame(list(zip(n,d,m,r)),columns = ['name','distance','mass','radius'])    
df.to_csv('scrapper_final.csv')