import requests
from bs4 import BeautifulSoup
import datetime

x=datetime.datetime.now()
headers={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"}
login_data={
"_token": "UapIrrtQqljfMY2aF6z31W1PWqvrrbzaYA8iqE7x",
"email": "asu@asucan.com",
"password":"1q2w3e4r"
}
with requests.Session() as s:
    url="https://www.oyunalisverisi.com/login"
    r=s.get(url,headers=headers)
    soup=BeautifulSoup(r.content,"html5lib")
    login_data["_token"]=soup.find("input",attrs={"name":"_token"})["value"]
    r=s.post(url,data=login_data,headers=headers)
    sp=BeautifulSoup(r.content,"lxml")
    selam=sp.find("a",{"class":"dropdown-toggle"}).text
    print("giriş yapan:{}tarih:{}".format(selam,x))
    print("*********************************************")










