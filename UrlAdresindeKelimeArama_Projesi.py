import re
import time
from urllib.request import urlopen
while 1:
    site =urlopen("https://www.dr.com.tr/Kitap/Kitab-ul-Hiyel/Ihsan-Oktay-Anar/Edebiyat/Roman/Turkiye-Roman/urunno=0000000061919")
    html=str(site.read())
    kelime=input("Aramak Istediginiz Kelimeyi Giriniz:")
    time.sleep(3) #4 sn sonra program calısmaya devam eder
    kelime_uzunlugu=len(re.findall(kelime,html))
    print("Url adresinde {} kelime sayisi: {}' dir\n".format(kelime,kelime_uzunlugu))
    print("*"*50)
    if (kelime_uzunlugu==0):
        print("!!!!!!!!!!!!!!!! Aramıs oldugunuz kelime Bu Url adresinde Mevcut Degil !!!!!!!!!!!!!!!!\n")
    devam_mi=input("Tekrar Kelime Aramak Istiyorsaniz Herhangi Bir Tusa Cikis Icın q' ya Basiniz:")
    if devam_mi=="q":
        break
