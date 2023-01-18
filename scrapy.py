import requests
from bs4 import BeautifulSoup

url = 'https://promotop.net/'

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}

site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')



url_pag = f'https://promotop.net/'
site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')
placas = soup.find_all('div', class_='grid_desc_and_btn')

with open('precos_placas.csv','a',newline='',encoding='UTF-8-sig') as f:
    for placa in placas:

        marca = placa.find('a', class_='re_track_btn').get_text().strip()

        try:
            preco = placa.find('span', class_='rh_regular_price').get_text().strip()
            num_preco = preco[:-3]

            loja = placa.find('span', class_='store_post_meta_item').get_text().strip()

        except:
            num_preco = '0'

        linha = marca + ';' + num_preco + ';' + loja + '\n'
        print(linha)
        f.write(linha)
        print(url_pag)




