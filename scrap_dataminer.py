import requests
import json
from bs4 import BeautifulSoup

for i in range(1,6):
    if i == 1:
        base_url = "https://dataminer.io/sandbox/index"
    else:
        base_url = "https://dataminer.io/sandbox/index{}".format(i)

    response = requests.get(base_url)

    html_soup = BeautifulSoup(response.text, 'html.parser')

    data = html_soup.findAll('div', attrs={"class": "person-container"})
    # print(len(data))


    for item in data:
        url = item.find('a')['href']
        if url == "matt_mullen":
            url = "profiles/" + url
        img = item.find('img')['src']
        
        name = item.find('h4').text.strip()
        poste = item.find('p', attrs={'class': 'title'}).text.strip()
        lieu = item.find('p', attrs={'class': 'location'}).text.strip()
        
        clearance = html_soup.find('p', attrs={'class': 'clearance'}).text.strip()
        experience = html_soup.find('p', attrs={'class': 'experience'}).text.strip()
        industry = html_soup.find('p', attrs={'class': 'industry'}).text.strip()
        
        biographie = html_soup.find('p', attrs={'class': 'bio-summery'}).text.strip()
        
        """detail code"""
        detail_url = "https://dataminer.io/sandbox/{}".format(url)
        res = requests.get(detail_url)

        detail_html_soup = BeautifulSoup(res.text, 'html.parser')
        
        full_description = detail_html_soup.find('div', attrs={'class': 'bio-container'}).text.strip()
        
        print(url, "\n", img, "\n", name, "\n", poste, "\n", lieu, "\n", clearance, "\n", experience, "\n", industry, "\n", biographie)
        print(full_description)