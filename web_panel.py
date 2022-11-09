import requests
import json

panel_web = "True"

def main():
    with open("config.json", 'r') as config:
        configs = json.load(config)
    with open("src/licence.json", 'r') as licence:
        licences = json.load(licence)
    response = requests.get('http://127.0.0.1/api/bot')
    requests.get(f'http://127.0.0.1/api/requets?serveur=1&statut=0')
    var = response.json()
    with open("config.json", 'w+') as configedit:
        configs["config"] = {}
        for name in var['links']:
            id = str(name['id'])
            configs["config"][str(name['name'])] = {}
            configs["config"][str(name['name'])]["id"] = str(name['id'])
            configs["config"][str(name['name'])]["url"] = str(name['url_vinted'])
            configs["config"][str(name['name'])]["webhook"] = str(name['url_integration'])
            requests.get(f'http://127.0.0.1/api/requets?etat=0&id={id}')
        json.dump(configs,configedit,indent=4)
    with open("src/licence.json", 'w+') as licenceedit:
        licences['licence'] = str(var['licence'])
        json.dump(licences,licenceedit,indent=4)

def update():
    with open("config.json", 'r') as config:
        configs = json.load(config)
    with open("src/licence.json", 'r') as licence:
        licences = json.load(licence)
    response = requests.get('http://127.0.0.1/api/bot')
    var = response.json()
    with open("config.json", 'w+') as configedit:
        configs["config"] = {}
        for name in var['links']:
            id = str(name['id'])
            configs["config"][str(name['name'])] = {}
            configs["config"][str(name['name'])]["id"] = str(name['id'])
            configs["config"][str(name['name'])]["url"] = str(name['url_vinted'])
            configs["config"][str(name['name'])]["webhook"] = str(name['url_integration'])
            requests.get(f'http://127.0.0.1/api/requets?etat=0&id={id}')
        json.dump(configs,configedit,indent=4)
    with open("src/licence.json", 'w+') as licenceedit:
        licences['licence'] = str(var['licence'])
        json.dump(licences,licenceedit,indent=4)

main()
