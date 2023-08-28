#Versão: 1.0
#Autor: Awdrix
#Contato: Discord - awdrix
#GitHub: https://github.com/ClippsComunnity/LinkCrawler
#linkedin: https://www.linkedin.com/in/adrielmcroberts/

import sys
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
def banner():
    ascii_art = """
    __    _       __   ______                    __         
   / /   (_)___  / /__/ ____/________ __      __/ /__  _____
  / /   / / __ \/ //_/ /   / ___/ __ `/ | /| / / / _ \/ ___/
 / /___/ / / / / ,< / /___/ /  / /_/ /| |/ |/ / /  __/ /    
/_____/_/_/ /_/_/|_|\____/_/   \__,_/ |__/|__/_/\___/_/     
                                                            
"""
    print(ascii_art)

def main():
    #Como usar o script
    if len(sys.argv) != 2:
        print("Uso: python linkcrawler.py [URL]")
        return

    #Coleta a url inserida pelo usuario 
    base_url = sys.argv[1]
    #divide a url para coletar só o nome do dominio
    parsed_url = urlparse(base_url)

    #A resposta do request até a separação do href dentro do html
    response = requests.get(base_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    links = soup.find_all('a', href=True)

    #Variaveis de ambiente
    clean_links = []
    domain_links = []
    out_links = []
    
    #Reorganiza e arruma os links
    for link in links:
        href = link.get('href')
        if not href.startswith('#'):
            if href not in clean_links:
                clean_links.append(href)

    for clean_link in clean_links:
        if clean_link.startswith(('http://', 'https://')):
            if parsed_url[1] in clean_link:
                domain_links.append(clean_link) #links de dentro do dominio
            else:
                out_links.append(clean_link) #links de fora do dominio
        else:
            domain_links.append(base_url + '/' + clean_link) #links de dentro do dominio
    
    #Printa os links de dentro e fora do dominio
    print('Links dentro do dominio')
    for item in domain_links:
        print(item)
        
    print("\n")

    print('Links fora do dominio')
    for item in out_links:
        print(item)

if __name__ == "__main__":
    banner()
    main()