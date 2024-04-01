import urllib.request
from bs4 import BeautifulSoup

url = "http://www-math.mit.edu/~gs/"
html = urllib.request.urlopen(url)
soup = BeautifulSoup(html)

tags = soup("a")

print("Enlaces en la página principal:\n")

# Primer nivel
for tag in tags:
    print(tag.text, tag.get("href"))

# Segundo nivel
print("\n Enlaces de las páginas secundarias: \n")
for tag in tags:
    newurl = tag.get("href")
    print(" Accediendo a los enlaces dentro de la página", newurl)
    try:
        if newurl[0:4]=="http":
            html2 = urllib.request.urlopen(newurl)
        else:
            html2 = urllib.request.urlopen(url+newurl)
        soup2 = BeautifulSoup(html2)
        newtags = soup2("a")
        if len(newtags) > 0:
            print(len(newtags)," enlaces:")
            for newtag in newtags:
                print(newtag.get("href"))
        else:
            print("No hay mas enlaces")
    except:
        print("Algo ha fallado")