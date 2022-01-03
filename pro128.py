from typing import final
from bs4 import BeautifulSoup 
from selenium import webdriver 
import time
import csv
import requests
starturl = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
browser = webdriver.Chrome("F:/api/c127-c128/venv/chromedriver.exe")

browser.get(starturl)
time.sleep(10)

headers =["Star_name", "Distance", "Mass", "Radius"]
star_data = []
new_star_data = []

def new_scrapper(hyperlink):
    for i in range(0,498):
        # while True:
        #     time.sleep(2)
        page = requests.get(hyperlink)
        soup = BeautifulSoup(page.text,"html.parser")
        for tr in soup.find_all("tr",attrs={"class":"fact_row"}):
            td_tag = tr.find_all("td")
            temp_list = []
            for td in td_tag:
                try:
                    temp_list.append(td.find_all("div",attrs={"class":"value"})[0].contents[0])
                except:
                    temp_list.append("")
            new_star_data.append(temp_list)
            

def scrapper():
    for i in range(0,4):
        soup= BeautifulSoup(browser.page_source,'html.parser')
        for ul in soup.find_all("ul",attrs={"class","exostar"}):
            li = ul.find_all("li")
            temp_list = []
            for index,li_tag in enumerate(li):
                if index == 0:
                    temp_list.append(li_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(li_tag.contents[0])
                    except:
                        temp_list.append("")
            hyperlink_li = li[0]
            temp_list.append("https://en.wikipedia.org/wiki/"+hyperlink_li.find_all("a",href=True)[0]["href"])
            star_data.append(temp_list)
        
               
scrapper()     

for h in star_data:
    new_scrapper(h[5])
    
final_star_data = []

for index,k in enumerate(star_data):
    final_star_data.append(k+final_star_data[index])
    
with open("data_final_pro128.csv",'w')as future_data:
    future_data_writter = csv.writer(future_data)
    future_data_writter.writerow(headers)
    future_data_writter.writerows(final_star_data)
    

