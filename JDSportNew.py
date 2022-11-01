import requests
import threading
import json
import time
def request(sex):
    headers = {
        'Host': 'www.jdsports.it',
        # Requests sorts cookies= alphabetically
        # 'Cookie': 'AKA_A2=A; language=it; 49746=; gdprsettings2={"functional":true,"performance":true,"targeting":true}; gdprsettings3={"functional":true,"performance":true,"targeting":true}; _gid=GA1.2.1156321040.1667319824; _gcl_au=1.1.35077614.1667319824; _scid=a5ee9ca0-e4bd-4b4d-ba88-c8130d95c448; _fbp=fb.1.1667319824933.890207719; RT="z=1&dm=jdsports.it&si=5f469e1d-332a-472d-b32e-acebcee6b38f&ss=l9yf65j7&sl=2&tt=2tq&obo=1"; _tt_enable_cookie=1; _ttp=0d7fab9c-1681-4430-bd30-24d3022d9bfe; _taggstar_ses=e06da51d-5a01-11ed-ad88-597f1616fa87; _taggstar_vid=e06da51d-5a01-11ed-ad88-597f1616fa87; mt.sc=%7B%22i%22%3A1667319982401%2C%22d%22%3A%5B%5D%7D; mt.v=2.1400177302.1667319982406; __pr.1prm=0rxWrK5Lbk; _uetsid=8e1d49c05a0111ed8e0fbbf564fe31f6; _uetvid=8e1d92b05a0111edb37305ec76b589ab; _ga=GA1.1.801295723.1667319824; cto_bundle=H6z80F9TNENMU1JuTE55WU1qQ2J3SXlzJTJCblFLQ0olMkJSQ0swbXBIdUVJZHZxaGQlMkY4N1BWeVh2UGk5bmNUd1ZuUlpHU2E1S3pkNkVaRk8xUDdKV2FhUTdUTmVsT1VQNkpWZWRKJTJGMzUyRWZLT29hUSUyRnh4c2M5QTdhYjdUV0pWa1lzT0RvNmlObXpIZFZrM2wyJTJGeHZHJTJCOU5aQkVKZyUzRCUzRA; _ga_2BLXMWYKY4=GS1.1.1667319823.1.1.1667320053.0.0.0',
        'cache-control': 'max-age=0',
        'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'referer': f'https://www.jdsports.it/{sex}/scarpe-{sex}/scarpe-sportive/',
        'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
    }

    params = {
        'sort': 'latest',
    }
    try:
        response = requests.get(f'https://www.jdsports.it/{sex}/scarpe-{sex}/scarpe-sportive/', params=params,headers=headers)
    except Exception as e:
        print(e)
    return response

def main(skus, sex):
    _skus = skus
    while True:
        new = fetchSkus(sex)
        for x in new:
            if x not in _skus:
                #send the webhook with all the fetched data 
                pass
        _skus = new
        time.sleep(0.1)
        

def fetchSkus(sex):
    r = request(sex)
    if r.status_code == 200: #added 200 just for testing purpose, on a regular basic every status code is checked
        lista = []
        j = (r.text.split('var dataObject = ')[1].split(';')[0])
        return lista #with all the skus
    print('Another status code occurred')
    return None

if __name__ == '__main__':
    sexes = ['uomo','donna']
    for sex in sexes:
        skus = fetchSkus(sex)
        if skus:
            Thread = threading.Thread(target = main, args = (skus, sex))
            Thread.name = 'New Prod JDSPORT'
            Thread.start
        else:
            print('Error fetchin skus')