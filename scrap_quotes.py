# importation des bibliothèques
import requests
from bs4 import BeautifulSoup
import json

"""
pip install requests
pip install bs4
"""


""" DEBUT PARTIE 1"""
base_url = "http://quotes.toscrape.com/"

response = requests.get(base_url)

# if response.ok:
#     print(response)
#     print(response.headers)
#     print(response.text)
"""FIN PARTIE 1"""

"""DEBUT PARTIE 2"""
base_url = "http://quotes.toscrape.com/"

response = requests.get(base_url)

quotes = {}

if response.ok:
    html_soup = BeautifulSoup(response.text, 'html.parser')
    
    # récupération des données
    datas = html_soup.findAll('div', attrs={'class': 'quote'})
    
    for data in datas:
        auteur = data.find('small', attrs={'class': 'author'})
        quote = html_soup.find('span', attrs={'class': 'text'})
        
        quotes[auteur.text] = quote.text


# ecriture des quotes dans un fichier txt
with open('quotes.txt', 'w', encoding='utf-8') as f:
    f.write("{\n")
    for k in quotes.keys():
        f.write("'{}':'{}'\n\n".format(k, quotes[k]))
    f.write("}")
"""FIN PARTIE2"""


"""DEBUT PARTIE 3"""
base_url = "http://quotes.toscrape.com/page/"
page_valid = True
quotes = {}
page = 1

while page_valid:
    page_url = base_url + str(page)
    
    response = requests.get(page_url)
    
    if "No quotes found!" in response.text:
        break
    
    html_soup = BeautifulSoup(response.text, 'html.parser')
    
    # récupération des données
    datas = html_soup.findAll('div', attrs={'class': 'quote'})
    
    for data in datas:
        auteur = data.find('small', attrs={'class': 'author'})
        quote = html_soup.find('span', attrs={'class': 'text'})
        
        quotes[auteur.text] = quote.text
    
    page += 1

# print(quotes)
# print(page)

# ecriture des quotes dans un fichier txt
with open('iter_quotes.txt', 'w', encoding='utf-8') as f:
    f.write("{\n")
    for k in quotes.keys():
        f.write("'{}':'{}'\n\n".format(k, quotes[k]))
    f.write("}")

# ecriture des quotes dans un fichier csv
# with open('iter_quotes.csv', 'w', encoding='utf-8') as csv_file:  
#     # writer = csv.writer(csv_file)
#     csv_file.write('Auteur,Citation\n')
#     for key, value in quotes.items():
#         csv_file.write(key + ',' + value + '\n')

"""FIN PARTIE 3"""