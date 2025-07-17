import requests


x = requests.get('https://w3schools.com/python/demopage.htm')

print(x)
print(x.encoding)

#headers
print(x.headers)

#funciones disponibles
print(dir(x))
