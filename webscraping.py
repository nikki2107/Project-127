from bs4 import BeautifulSoup
import time
import csv
import requests
import pandas as pd

START_URL="https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars/"
page = requests.get(START_URL)
print(page)

soup = BeautifulSoup(page.text,"html.parser")
star_table=soup.find('table')

temp_list=[]
table_rows=star_table.find_all('tr')
for tr in table_rows:
    td=tr.find_all('td')
    row=[i.text.rstrip() for i in td]
    temp_list.append(row)
    
S=[]
D=[]
M=[]
R=[]
L=[]

for i in range(1,len(temp_list)):
    S.append(temp_list[i][1])
    D.append(temp_list[i][3])
    M.append(temp_list[i][5])
    R.append(temp_list[i][6])
    L.append(temp_list[i][7])
    
df2=pd.DataFrame(list(zip(S,D,M,R,L)),columns=['S','D','M','R','L'])
print(df2)
df2.to_csv('bright_stars.csv')  
    
