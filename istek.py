import requests
from bs4 import BeautifulSoup

url=("https://www.arabam.com/ikinci-el/otomobil/alfa-romeo","https://www.arabam.com/ikinci-el/otomobil/anadol","https://www.arabam.com/ikinci-el/otomobil/aston-martin","https://www.arabam.com/ikinci-el/otomobil/audi","https://www.arabam.com/ikinci-el/otomobil/bentley","https://www.arabam.com/ikinci-el/otomobil/bmw","https://www.arabam.com/ikinci-el/otomobil/citroen","https://www.arabam.com/ikinci-el/otomobil/dacia","https://www.arabam.com/ikinci-el/otomobil/fiat","https://www.arabam.com/ikinci-el/otomobil/ford","https://www.arabam.com/ikinci-el/otomobil/honda","https://www.arabam.com/ikinci-el/otomobil/hyundai","https://www.arabam.com/ikinci-el/otomobil/kia","https://www.arabam.com/ikinci-el/otomobil/lada","https://www.arabam.com/ikinci-el/otomobil/mercedes-benz","https://www.arabam.com/ikinci-el/otomobil/mini","https://www.arabam.com/ikinci-el/otomobil/mitsubishi","https://www.arabam.com/ikinci-el/otomobil/nissan","https://www.arabam.com/ikinci-el/otomobil/opel","https://www.arabam.com/ikinci-el/otomobil/peugeot","https://www.arabam.com/ikinci-el/otomobil/renault","https://www.arabam.com/ikinci-el/otomobil/toyota","https://www.arabam.com/ikinci-el/otomobil/volkswagen","https://www.arabam.com/ikinci-el/otomobil/volvo")
for i in url:
    r = requests.get(i)
    print(r.status_code)
    soup=BeautifulSoup(r.content,"lxml")

    arabalar=soup.find_all("li",attrs={"class":"category-facet-selection-item outside-li disabled"})
    for araba in arabalar:

        isim = araba.find("a", attrs={"class": "list-item"}).text.strip()
        marka = soup.find("h2", attrs={"class": "dib"}).text.strip()

        kayit={"marka":marka,"model":isim}

        print(kayit)
















