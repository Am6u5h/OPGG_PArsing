import requests
from bs4 import BeautifulSoup
import json
import csv

# url = 'https://ru.op.gg/champions'
#
headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.66 Safari/537.36 Edg/103.0.1264.44"

}
# req = requests.get(url,headers=headers)
# src = req.text
# print(src)
#
# with open("index.html","w",encoding="utf-8") as file:
#     file.write(src)

# with open("index.html",encoding="utf-8") as file:
#     src = file.read()
#
# soup = BeautifulSoup(src, "lxml")
# all_champions_hrefs = soup.find_all(class_="css-mtyeel e1y3xkpj0")
#
# all_champions_dict = {}
# for champ in all_champions_hrefs:
#     champ_text = champ.text
#     champ_href = "https://ru.op.gg/" + champ.get("href")
#     all_champions_dict[champ_text] = champ_href
#     #print(f"{champ_text}:{champ_href}")
# with open("all_champions_dict.json","w",encoding="utf-8") as file:
#     json.dump(all_champions_dict,file,indent=4, ensure_ascii=False)

with open("all_champions_dict.json", encoding="utf-8") as file:
    all_champions = json.load(file)

count = 0
#champ_name = input("Введите имя чемпиона: ")
for champion_name,champion_href in all_champions.items():

    if count == 0:
        rep = [". ", "'", " & "," "]
        for item in rep:
            if item in champion_name:
                champion_name = champion_name.replace(item, "_")
                #print(champion_name)
        req = requests.get(url=champion_href,headers=headers)
        src = req.text

        with open(f"data/{count}_{champion_name}.html", "w",encoding="utf-8") as file:
            file.write(src)

        with open(f"data/{count}_{champion_name}.html",encoding="utf-8") as file:
            src = file.read()

        soup = BeautifulSoup(src, "lxml")

        table_head = soup.find(class_="css-104mws0 epbr24v3").find_all("img")
        all_tables = soup.find_all(class_="css-104mws0 epbr24v3")
        builds_name = soup.find_all("caption")
        k = 0
        names_dict = []
        print("    " + champion_name)
        for itembuild in all_tables:
            items = itembuild.find_all("img")
            names = str(itembuild.find("caption"))
            names = names.replace('<caption>', '')
            names = names.replace('</caption>', '')
            names_dict.append(names)

            print("**************")
            print(names)
            print("--------------")
            for item in items:
                res = item.get("alt")
                print(res)
                k+=1
                if k%3==0 and names == "Recommended Builds":
                    print("-----------------")

        with open(f"data/{count}_{champion_name}.csv","w", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(
                (
                    "Champion",
                    names_dict[0],
                    '',
                    names_dict[1],
                    '',
                    names_dict[2],

                )
            )









        count+= 1

