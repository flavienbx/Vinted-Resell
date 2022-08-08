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

with open("config.json", 'r') as config:
    configs = json.load(config)
n_max = 0
for name in configs["config"]:
    n_max += 1
n_max = n_max

class Spy:
    gris = "\033[1;30;1m"
    rouge = "\033[1;31;1m"
    vert = "\033[1;32;1m"
    jaune = "\033[1;33;1m"
    bleu = "\033[1;34;1m"
    violet = "\033[1;35;1m"
    cyan = "\033[1;36;1m"
    blanc = "\033[1;0;1m"

asciiart = f"""{Spy.rouge}
██████╗  ██████╗ ████████╗
██╔══██╗██╔═══██╗╚══██╔══╝
██████╔╝██║   ██║   ██║   
██╔══██╗██║   ██║   ██║   
██████╔╝╚██████╔╝   ██║   
╚═════╝  ╚═════╝    ╚═╝   
"""

with open("src/ver.json", 'r') as config:
    ver = json.load(config)
    version = ver['ver']
    r = requests.get('https://raw.githubusercontent.com/flavienbx/Vinted-Resell/main/src/ver.json')
    ver_data = r.json()
    if ver['ver'] != ver_data['ver']:
        try:
            os.system('cls')
            os.system('title Dev by Flavien')
        except:
            os.system('clear')
        print(asciiart + "\n\n")
        print(f"{Spy.gris}[{Spy.rouge}ATTENTION{Spy.gris}] Le bot n'est pas à jour ! (Version actuel : {Spy.blanc}{ver_data['ver']}{Spy.gris} Version du bot : {Spy.blanc}{ver['ver']}{Spy.gris})")
        print(f"{Spy.gris}[{Spy.violet}MISE À JOUR{Spy.gris}] Liens du github : {Spy.blanc}https://github.com/flavienbx/Vinted-Resell{Spy.gris}")
        os.system('pause')

url_avatar_webhook = "https://www.techwikies.com/wp-content/uploads/2019/04/Vinted.png"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--mute-audio")
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.set_window_size(1024, 650)

with open('src/n.json') as f:
    data = json.load(f)
n = data["n"]
if n >= n_max:
    n = 1


def get_item_info(webhook):
    try:
        try:
            os.system('cls')
            os.system('title Dev by Flavien')
        except:
            os.system('clear')
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
            if n >= n_max:
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
    with open("config.json", 'r') as config:
        configs = json.load(config)
    temp_n_max = 0
    for name in configs["config"]:
        temp_n_max += 1
        if temp_n_max == n:
            url_search = configs['config'][name]['url']
            webhook = configs['config'][name]['webhook']
    driver.get(url_search)
    #pre = driver.find_element_by_tag_name("pre").text
    pre = driver.find_element(By.TAG_NAME, "pre").text
    data = json.loads(pre)
    with open('src/temp.json', 'w') as j:
        json.dump(data, j)
    get_item_info(webhook)

get_item()
