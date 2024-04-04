# importando bibliotecas para webscraping
import requests
from bs4 import BeautifulSoup

# link da página do site
url = 'https://www.amazon.com.br/gp/bestsellers/electronics/ref=zg_bs_electronics_sm'

# meu user agent
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
    (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 OPR/107.0.0.0'}


site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')

def next_page(soup):
    # procurar o botão próximo
    pag = soup.find('a', {'class':"a-letter-space"})
    
    # ir na ultima página com o botão "próximo" está desativado
    if not pag.find('span', {'class':'a-disabled a-last'}):
        
        # url do site home page
        url = 'https://www.amazon.com.br/'
        
        # botão de próximo que possua href
        next = soup.find('a', "a-letter-space", href = True)
        
        # link final com href
        final_url = (url + str(next['href']))
        
        return final_url
    
    else:
        return
    
# iteragindo
site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')
url = next_page(soup)

print(url)