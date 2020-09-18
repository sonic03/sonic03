import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

indexler=[]
kriter = ["Level", "Kupa", "İnşaatçı", "Barbar Kral", "Okçu Kraliçe", "Askeri Yükseltme", "Duvar Yükseltmeleri",
          "Köy Binası"]


def klans(url):





    fiyat=[]
    r=requests.get(u)
    print(r.status_code)

    soup=BeautifulSoup(r.content,"lxml")


    bilgi=soup.find_all(style="color:#000;")

    for bil in bilgi:
        bil=str(bil)
        bil=bil.replace('<b style="color:#000;">',"")
        bil=bil.replace('</b>',"")

        fiyat.append(bil)


    #i=pd.DataFrame(data=fiyat,index=kriter)

    print(bil)
    indexler.append(fiyat)


url=["https://hesapsatis.com/ilan/139910-12lvl-5lvl-giga-tesla-hesap-satisi/","https://hesapsatis.com/ilan/142550-120tl-140-seviye-kb-11/","https://hesapsatis.com/ilan/142887-210level-full-14-lvl-duvar-full-8-kostumlu-kacirma","https://hesapsatis.com/ilan/139129-clash-of-clans-th13-207-level/","https://hesapsatis.com/ilan/132974-110-level-8200-elmas/"]

for u in url:

    klans(u)


print(indexler)

cc=pd.DataFrame(data=indexler[0],index=kriter)
for i in range(len(url)):
    cc["hesap-"+str(i)]=indexler[i]
    i+=1
"""cc["col2"]=indexler[1]
cc["col3"]=indexler[2]
cc[]"""
#print(cc)
cc.drop(0,axis=1,inplace=True)
print(cc)
print(cc.columns)
