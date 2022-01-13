import requests
from bs4 import BeautifulSoup
from time import sleep

#fazendo o request dos projetos do site matheusportfolio.me
#testando o requests


response = requests.get("http://matheusportfolio.me/")

content = response.content
site = BeautifulSoup(content, 'html.parser')
row = site.find('div', attrs={'class': 'row'})
cardbodys = row.findAll('div', attrs={'class': 'card-body'})
detalhes = []
print('PROJETOS')
print()
for cardbody in cardbodys:
    titulo = cardbody.find('p', attrs={'class':'card-text'}).text
    lis = cardbody.find('ul').findAll('li')
    print(titulo)
    for lis in lis:
        print(lis.text)
    print()

container = site.findAll('div', attrs={'class': 'container'})
container = container[2]
sobremim = container.find('h2').text
print(sobremim.upper())
print()
texto_sobre_autor = container.find('p', attrs={'class': 'lead textoBranco'}).text
print(texto_sobre_autor)