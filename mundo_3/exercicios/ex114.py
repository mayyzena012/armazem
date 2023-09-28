#

import requests

def checar():
    url = "https://www.cursoemvideo.com"

    try:
        requests.get(url)
        return True

    except ConnectionError:
        return False

    

if checar():
    print("Pudim esta acessivel")
else:
    print("Pudim nao esta acessivel")
