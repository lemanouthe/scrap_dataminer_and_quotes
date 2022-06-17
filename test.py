import requests
import json
from bs4 import BeautifulSoup


result = []

for n in range(1,24):
    base_url = "https://walletconnect.com/registry?page={}".format(n)
    # print(base_url)


    response = requests.get(base_url)

    # print(response.status_code)

    html_soup = BeautifulSoup(response.text, 'html.parser')
    # print(html_soup)

    script_data = html_soup.find('script', attrs={'id': "__NEXT_DATA__"})
    data = json.loads(script_data.get_text())
    # print(data)
    cpt = 0
    for item in data['props']['pageProps']['listings']:
        # print(item)
        url = item['homepage']
        name = item['name']
        image = item['image']
        result.append(url)
        result.append(name)
        result.append(image)
        
        print('---')
        
        print(cpt, "\n" +"url : " +url +"\n"+ "image : " +image +"\n"+ "name : " +name +"\n")
        cpt += 1
    # print(result)
with open('readme.txt', 'w', encoding='utf-8') as f:
    for line in result:
        f.write(line)
        f.write('\n')