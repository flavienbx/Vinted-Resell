from glob import glob
from lib2to3.pgen2 import driver
from pickle import TRUE
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from discord_webhook import DiscordWebhook, DiscordEmbed
from os import system, name
import chromedriver_binary
import requests
from time import time, strftime, gmtime, sleep
import pyfiglet, os, threading
import json


url1 = "https://www.vinted.fr/api/v2/catalog/items?search_text=jordan&catalog_ids=1242&color_id[]=5&brand_ids=&size_ids=&material_ids=&status_ids=&country_ids=&city_ids=&is_for_swap=&currency=&price_to=&price_from=&page=1&per_page=1&order=newest_first"
webhook1 = "https://discord.com/api/webhooks/1005735666006642760/oWlc7ZyDxK_rEiUyfWlC4TK8nz6V2OPC94J7_gsC_t3_I504I8H6Innk_XGn7AM03JAB"

url2 = "https://www.vinted.fr/api/v2/catalog/items?search_text=&catalog_ids=79&color_id[]=&brand_ids=&size_ids=&material_ids=&status_ids=&country_ids=&city_ids=&is_for_swap=&currency=&price_to=&price_from=&page=1&per_page=1&order=newest_first"
webhook2 = "https://discord.com/api/webhooks/1005739017649799178/NKXob7AzhZPOLyiVJ8LIbeff8FfxNKF_snV_6eg7SyL_cM2ncvuhwxCAg0auPsVDyefe"

class Spy:
    gris = "\033[1;30;1m"
    rouge = "\033[1;31;1m"
    vert = "\033[1;32;1m"
    jaune = "\033[1;33;1m"
    bleu = "\033[1;34;1m"
    violet = "\033[1;35;1m"
    cyan = "\033[1;36;1m"
    blanc = "\033[1;0;1m"

url_avatar_webhook = "https://www.techwikies.com/wp-content/uploads/2019/04/Vinted.png"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--mute-audio")
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.set_window_size(1024, 650)

with open('src/n.json') as f:
    data = json.load(f)
n = data["n"]
if n >= 2:
    n = 1

def get_item_info(webhook):
    try:
        try:
            os.system('cls')
            os.system('title Dev by Flavien')
        except:
            os.system('clear')



        asciiart = f"""{Spy.rouge}
        ██████╗  ██████╗ ████████╗
        ██╔══██╗██╔═══██╗╚══██╔══╝
        ██████╔╝██║   ██║   ██║   
        ██╔══██╗██║   ██║   ██║   
        ██████╔╝╚██████╔╝   ██║   
        ╚═════╝  ╚═════╝    ╚═╝   
        """

        print(asciiart + "\n\n")
        with open('src/temp.json') as mon_fichier:
            print(f"{Spy.blanc}[{Spy.jaune}RECHERCHE{Spy.blanc}] - Le bot recupere les informations de l'item...")
            data = json.load(mon_fichier)

            data2 = data['items']
            id = data2[0]['id'] #id de vente
            sleep(0.5)
            title = data2[0]['title'] #titre
            brand_title = data2[0]['brand_title'] #marque
            price = data2[0]['price'] #prix
            currency = data2[0]['currency'] #Money
            data3 = data2[0]['user'] #user
            sleep(0.5)
            profil_url = data3['profile_url'] #url du profil vendeur
            auteur = data3['login'] #nom du vendeur
            url = data2[0]['url'] #url du produit
            size = data2[0]['size_title'] #taille
            data4 = data2[0]['photo']
            image_photo = data4['url'] #image du produit
            if currency == "EUR":
                devise = "€"
            else:
                devise = ""
            sleep(1)
        try:
            with open('src/n.json') as f:
                data = json.load(f)
            n = data["n"]
            if n >= 2:
                n = 0
            n = n + 1

            data = {'n':n}
            with open("src/n.json", 'w') as f:
                json.dump(data, f)
        except:
            pass

        try:
            with open("src/data.json") as f:
                jdat = json.load(f)

            if id in jdat["id"]:
                print(f"{Spy.blanc}[{Spy.rouge}ATTENTION{Spy.blanc}] - Item déjà envoyé !")
                sleep(30)
                driver.refresh()
                get_item()
            else:
                jdat["id"].append(id)
                with open("src/data.json", 'w') as f:
                    json.dump(jdat, f)
            sleep(2)

            webhook = DiscordWebhook(url=webhook, username="Vinted", avatar_url=url_avatar_webhook)
            embed = DiscordEmbed(title='', description=f'[```YAML\n👕 {title}```]({url})', color='03b2f8')
            embed.set_footer(text='Bot by Flavien')
            embed.set_timestamp()
            embed.add_embed_field(name='**``💶`` Prix**', value=f'[```YAML\n{price}{devise}```]({url})', inline=True)
            embed.add_embed_field(name='**``📏`` Taille**', value=f'[```YAML\n{size}```]({url})', inline=True)
            embed.add_embed_field(name='**``🔖`` Marque**', value=f'[```YAML\n{brand_title}```]({url})', inline=True)
            embed.add_embed_field(name='**``👨`` Auteur**', value=f'[```YAML\n{auteur}```]({profil_url})', inline=True)
            embed.set_thumbnail(url=f'{image_photo}')

            webhook.add_embed(embed)
            response = webhook.execute()     
            print(f"{Spy.blanc}[{Spy.vert}INFORMATION{Spy.blanc}] - Nouvel item trouvé !")
            sleep(2)
            driver.refresh()
            get_item()
        except:
            sleep(1)
            driver.refresh()
            get_item()
    except:
        sleep(1)
        driver.refresh()
        get_item()

try:
    os.system('cls')
except:
    os.system('clear')

def get_item():
    try:
        os.system('title Bot Vinted')
    except:
        pass
    posting = []
    driver.get("https://www.vinted.fr/")
    with open('src/n.json') as f:
        data = json.load(f)
    n = data["n"]
    if n == 1:
        url_search = url1
        webhook = webhook1
    elif n == 2:
        url_search = url2
        webhook = webhook2
    driver.get(url_search)
    pre = driver.find_element_by_tag_name("pre").text
    data = json.loads(pre)
    with open('src/temp.json', 'w') as j:
        json.dump(data, j)
    get_item_info(webhook)

get_item()