from web_panel import *
from main import *
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
try:
    if(panel_web):
        pass
except:
    panel_web = "False"

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
        if (panel_web=="True"):
            requests.get(f'http://127.0.0.1/api/requets?serveur=1&statut=2')
        try:
            os.system('cls')
        except:
            os.system('clear')
        print(asciiart + "\n\n")
        print(f"{Spy.gris}[{Spy.rouge}ATTENTION{Spy.gris}] Le bot n'est pas à jour ! (Version actuel : {Spy.blanc}{ver_data['ver']}{Spy.gris} Version du bot : {Spy.blanc}{ver['ver']}{Spy.gris})")
        print(f"{Spy.gris}[{Spy.violet}MISE À JOUR{Spy.gris}] Liens du github : {Spy.blanc}https://github.com/flavienbx/Vinted-Resell{Spy.gris}")
        os.system('pause')
    else:
        if (panel_web=="True"):
            requests.get(f'http://127.0.0.1/api/requets?serveur=1&statut=1')

exec(base64.b64decode("aWYoQVBJX1JldHVybl9QTEFOX25hbWUgPT0gIlZpbnRlZCAtIFJlc2VsbCIpOgogICAgdXJsX2F2YXRhcl93ZWJob29rID0gImh0dHBzOi8vd3d3LnRlY2h3aWtpZXMuY29tL3dwLWNvbnRlbnQvdXBsb2Fkcy8yMDE5LzA0L1ZpbnRlZC5wbmciCiAgICBjaHJvbWVfb3B0aW9ucyA9IHdlYmRyaXZlci5DaHJvbWVPcHRpb25zKCkKICAgIGNocm9tZV9vcHRpb25zLmFkZF9hcmd1bWVudCgiLS1tdXRlLWF1ZGlvIikKICAgIGNocm9tZV9vcHRpb25zLmFkZF9leHBlcmltZW50YWxfb3B0aW9uKCdleGNsdWRlU3dpdGNoZXMnLCBbJ2VuYWJsZS1sb2dnaW5nJ10pCiAgICBkcml2ZXIgPSB3ZWJkcml2ZXIuQ2hyb21lKENocm9tZURyaXZlck1hbmFnZXIoKS5pbnN0YWxsKCkpCiAgICBkcml2ZXIuc2V0X3dpbmRvd19zaXplKDEwMjQsIDY1MCkKCiAgICB3aXRoIG9wZW4oJ3NyYy9uLmpzb24nKSBhcyBmOgogICAgICAgIGRhdGEgPSBqc29uLmxvYWQoZikKICAgIG4gPSBkYXRhWyJuIl0KICAgIGlmIG4gPj0gbl9tYXg6CiAgICAgICAgbiA9IDE="))

def get_item_info(webhook):
    try:
        try:
            os.system('cls')
        except:
            os.system('clear')
        print(asciiart + "\n\n")
        with open('src/temp.json') as mon_fichier:
            print(f"{Spy.blanc}[{Spy.jaune}RECHERCHE{Spy.blanc}] - Le bot recupere les informations de l'item...")
            data = json.load(mon_fichier)

            data2 = data['items']
            id = data2[0]['id']
            sleep(0.5)
            title = data2[0]['title']
            brand_title = data2[0]['brand_title']
            if data2[0]['brand_title'] == "":
                brand_title = "Aucune"
            else:
                brand_title = data2[0]['brand_title']
            price = data2[0]['price']
            currency = data2[0]['currency']
            data3 = data2[0]['user']
            sleep(0.5)
            profil_url = data3['profile_url']
            auteur = data3['login']
            url = data2[0]['url']
            if data2[0]['size_title'] == "":
                size = "Aucune"
            else:
                size = data2[0]['size_title']
            data4 = data2[0]['photo']
            image_photo = data4['url']
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

            webhook = DiscordWebhook(url=webhook, username=API_Return_PLAN_name, avatar_url=API_Return_PLAN_Image)
            embed = DiscordEmbed(title='', description=f'[\n👕 {title}]({url})', color='03b2f8')
            embed.set_footer(text=f'{API_Return_INTEGRATION_DiscordUsername}#{API_Return_INTEGRATION_DiscordDiscriminator}', icon_url=API_Return_INTEGRATION_DiscordAvatar)
            embed.set_timestamp()
            embed.add_embed_field(name='**``💶`` Prix**', value=f'[\n{price}{devise}]({url})', inline=True)
            embed.add_embed_field(name='**``📏`` Taille**', value=f'[\n{size}]({url})', inline=True)
            embed.add_embed_field(name='**``🔖`` Marque**', value=f'[\n{brand_title}]({url})', inline=True)
            embed.add_embed_field(name='**``👨`` Auteur**', value=f'[\n{auteur}]({profil_url})', inline=True)
            #embed.set_thumbnail(url=f'{image_photo}')
            embed.set_image(url=f'{image_photo}')

            webhook.add_embed(embed)
            response = webhook.execute()     
            print(f"{Spy.blanc}[{Spy.vert}INFORMATION{Spy.blanc}] - Nouvel item trouvé !")
            sleep(2)
            if (panel_web=="True"):
                update()
                sleep(1)
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

def TransformApi(url):
    url = url.replace("https://www.vinted.fr/vetements", "https://www.vinted.fr/api/v2/catalog/items")
    url = url.replace("id[]", "ids")
    url = url.replace("[]", "_ids")
    url = url.replace("&order=price_high_to_low", "&order=newest_first")
    url = url.replace("&order=price_low_to_high", "&order=newest_first")
    url = url.replace("&order=relevance", "&order=newest_first")
    url = url + "&page=1&per_page=1"
    return url
    
def get_item():
    posting = []
    driver.get("https://www.vinted.fr/")
    try:
        os.system('cls')
    except:
        os.system('clear')
    print(asciiart + "\n\n")
    with open('src/n.json') as f:
        data = json.load(f)
    n = data["n"]
    with open("config.json", 'r') as config:
        configs = json.load(config)
    temp_n_max = 0
    for name in configs["config"]:
        temp_n_max += 1
        if (panel_web=="True"):
            id = configs['config'][name]['id']
            requests.get(f'http://127.0.0.1/api/requets?etat=1&id={id}')
        if temp_n_max == n:
            url_search = configs['config'][name]['url']
            webhook = configs['config'][name]['webhook']
            if (panel_web=="True"):
                id = configs['config'][name]['id']
                requests.get(f'http://127.0.0.1/api/requets?etat=2&id={id}')
    driver.get(TransformApi(url_search))
    #pre = driver.find_element_by_tag_name("pre").text
    pre = driver.find_element(By.TAG_NAME, "pre").text
    data = json.loads(pre)
    with open('src/temp.json', 'w') as j:
        json.dump(data, j)
    get_item_info(webhook)

get_item()
