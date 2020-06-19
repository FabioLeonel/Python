#AULA 23 (esta na pasta modulos)
import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://pudim.com.br')
except urllib.error.URLError:
    print('O site Pudim não está acessível')
else:
    print('Consegui acessar o site')
    print(site.read())
