# crie um código em pyhton que teste se o site Pudim está acessivel pelo computador usado
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('site offline')
else:
    print('site online')
