import requests
from bs4 import BeautifulSoup

import json
import time

url = 'https://ru.op.gg/champions'
champ_name = input("На кого искать билд? Введите имя чемпиона: ")

headers = {
    "Accept": "*/*",
    #"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.66 Safari/537.36 Edg/103.0.1264.44"
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"

}
req = requests.get(url,headers=headers)
src = req.text
#print(src)

soup = BeautifulSoup(src, "lxml")
all_champions_hrefs = soup.find_all(class_="css-mtyeel e1y3xkpj0")

all_champions_dict = {}
for champ in all_champions_hrefs:
    champ_text = champ.text
    champ_href = "https://ru.op.gg/" + champ.get("href")
    all_champions_dict[champ_text] = champ_href
    #print(f"{champ_text}:{champ_href}")

print(champ_name + ": " + all_champions_dict.get(champ_name))


request = requests.get(all_champions_dict.get(champ_name),headers=headers)
src1 = request.text
#print(src1)

soup1 = BeautifulSoup(src1,"lxml")

#all_tables = soup1.find_all(class_="css-104mws0 epbr24v3")
all_tables = soup1.find_all(class_="css-1yie7qw epbr24v3")
builds_name = soup1.find_all("caption")

names_dict = []
#print("    " + champ_name)
#print(all_tables)
for itembuild in all_tables:
        items = itembuild.find_all("img")
        names = str(itembuild.find("caption"))
        names = names.replace('<caption>', '')
        names = names.replace('</caption>', '')
        names_dict.append(names)

        print("--------------")
        print(names)
        print("--------------")
        k = 0
        for item in items:
            res = str(item.get("alt"))
            if names == "Recommended Builds" and (res == "Dark Seal" or res =="Tear of the Goddess"):
                pass
            else:
                print(" * " + res)
                k+=1
                if k%3==0 and names == "Recommended Builds":
                    print("-----------------")


time.sleep(300)
