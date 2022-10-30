import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
mydb = client["database"]  # all adında bir database

mycol = mydb["ürün"]  # product adında bir koleksiyon
mycol1 = mydb["marka"]
mycol2 = mydb["ram"]
mycol3 = mydb["isletimsistemi"]
mycol4 = mydb["islemcitipi"]
mycol5 = mydb["diskboyutu"]
mycol6 = mydb["ekrankartitipi"]
mycol7 = mydb["ekrancozunurluk"]
mycol8 = mydb["fiyat"]
mycol9 = mydb["puan"]

urun = list()
marka = list()
ram = list()
isletimsistemi = list()
islemcitipi = list()
diskboyutu = list()
ekrankartitipi = list()
ekrancozunurluk = list()
fiyat = list()# aynı olmayabilir
puan = list()#vatan n1

for i in range(1, 18):
    number = i
    r2 = requests.get("https://www.vatanbilgisayar.com/notebook/?page=" + str(number) + "")  # ilk request
    soup2 = BeautifulSoup(r2.content, "lxml")
    st2 = soup2.find("div",
                     attrs={'id': 'productsLoad', 'class': 'wrapper-product wrapper-product--list-page clearfix'})

    for linkler in st2.find_all("a", class_="product-list__link"):
        link_sonu = linkler.get('href')
        link_basi = "https://www.vatanbilgisayar.com/"
        link = link_basi + link_sonu
        # print(link)
        r3 = requests.get(link)  # 3.request
        soup3 = BeautifulSoup(r3.content, "lxml")

        # product = soup3.find("div", class_="product-list__content product-detail-big-price").find("h1",class_="product-list__product-name").text
        # brand = soup3.find("div", class_="wrapper-product-brand").find("img").get("title")
        # price = soup3.find("span", class_="product-list__price").text + " TL"
        # print(product),#"Fiyat:" + price, "Marka:" + brand
        urun.append(soup3.find("div", class_="product-list__content product-detail-big-price").find("h1", class_="product-list__product-name").text)
        marka.append(soup3.find("div", class_="wrapper-product-brand").find("img").get("title"))
        fiyat.append(soup3.find("span", class_="product-list__price").text + " TL")
        puan.append(soup3.find("div", class_="col-lg-8 col-md-8 col-sm-8 col-xs-12").find("strong", attrs={'id': 'averageRankNum'}).text)

        teknik_ayrıntılar = soup3.find_all("tr", attrs={"data-count": "0"})
        string = ""
        for i in teknik_ayrıntılar:
            etiket = i.find("td").text
            deger = i.find("p").text
            string = etiket + ": " + deger + ";"
            # print(string)
            a = string.rfind("Ram (Sistem Belleği):")
            if (a >= 0):
                # print(a)
                c = string.find(";")
                ram.append(string[a + 21:a + c])
                # print(ram)

            a = string.rfind("İşletim Sistemi:")
            if (a >= 0):
                # print(a)
                c = string.find(";")
                isletimsistemi.append(string[a + 16:a + c])
                # print(isletimsistemi)

            a = string.rfind("İşlemci Teknolojisi:")
            if (a >= 0):
                # print(a)
                c = string.find(";")
                islemcitipi.append(string[a + 20:a + c])
                # print(islemcitipi)

            a = string.rfind("Disk Kapasitesi:")
            if (a >= 0):
                # print(a)
                c = string.find(";")
                diskboyutu.append(string[a + 16:a + c])
                # print(diskboyutu)

            a = string.rfind("Ekran Kartı Tipi:")
            if (a >= 0):
                # print(a)
                c = string.find(";")
                ekrankartitipi.append(string[a + 17:a + c])
                # print(ekrankartitipi)

            a = string.rfind("Çözünürlük (Piksel):")
            if (a >= 0):
                # print(a)
                c = string.find(";")
                ekrancozunurluk.append(string[a + 20:a + c])
                # print(ekrancozunurluk)

############################################################################################################################

numbers = [1, 2, 4, 5, 6, 7, 8, 10, 12, 13]  # 3ve9.site html kodları bozuk
for i in numbers:
    number = i
    r = requests.get(
        "https://www.trendyol.com/sr?wc=103108&qt=bilgisayar&st=bilgisayar&os=1&pi=" + str(number) + "")  # ilk request
    soup = BeautifulSoup(r.content, "lxml")
    st1 = soup.find("div", attrs={"class": "prdct-cntnr-wrppr"})
    for linkler in st1.find_all('a'):
        link_sonu = linkler.get('href')
        link_basi = "https://www.trendyol.com/"
        link = link_basi + link_sonu
        # print(link)

        r1 = requests.get(link)  # 2.request
        soup1 = BeautifulSoup(r1.content, "lxml")

        # product = soup1.find("h1", attrs={'data-drroot': 'h1', 'class': 'pr-new-br'}).text
        # brand = soup1.find("h1", class_="pr-new-br").find("a").text
        # price = soup1.find("span", class_="prc-dsc").text
        # print("Fiyat:" + price, "Marka:" + brand, properties)
        urun.append(soup1.find("h1", attrs={'data-drroot': 'h1', 'class': 'pr-new-br'}).text)
        marka.append(soup1.find("h1", class_="pr-new-br").find("a").text)
        fiyat.append(soup1.find("span", class_="prc-dsc").text)

        teknik_ayrıntılar = soup1.find_all("li", attrs={"class": "detail-attr-item"})
        string = ""
        for i in teknik_ayrıntılar:
            etiket = i.find("span").text
            deger = i.find("b").text
            string = etiket + ": " + deger + ";"
            # print(string)

            a = string.rfind("Ram (Sistem Belleği):")
            if (a >= 0):
                # print(a)
                c = string.find(";")
                ram.append(string[a + 21:a + c])
                # print(ram)
            a = string.rfind("İşletim Sistemi:")
            if (a >= 0):
                # print(a)
                c = string.find(";")
                isletimsistemi.append(string[a + 16:a + c])
                # print(isletimsistemi)

            a = string.rfind("İşlemci Tipi:")
            if (a >= 0):
                # print(a)
                c = string.find(";")
                islemcitipi.append(string[a + 13:a + c])
                # print(islemcitipi)

            a = string.rfind("SSD Kapasitesi:")
            if (a >= 0):
                # print(a)
                c = string.find(";")
                diskboyutu.append(string[a + 15:a + c])
                # print(diskboyutu)

            a = string.rfind("Ekran Kartı Tipi:")
            if (a >= 0):
                # print(a)
                c = string.find(";")
                ekrankartitipi.append(string[a + 17:a + c])
                # print(ekrankartitipi)

            a = string.rfind("Çözünürlük:")
            if (a >= 0):
                # print(a)
                c = string.find(";")
                ekrancozunurluk.append(string[a + 11:a + c])
                # print(ekrancozunurluk)

############################################################################################################################
for i in range(2, 30):
    number = i
    r4 = requests.get("https://www.n11.com/arama?q=notebook&ipg=" + str(number) + "")  # ilk request
    soup4 = BeautifulSoup(r4.content, "lxml")

    for linkler in soup4.find_all("span", class_="oldPrice noLine cPoint priceEventClick"):
        link = linkler.get('data-href')
        # print(link)
        r5 = requests.get(link)
        soup5 = BeautifulSoup(r5.content, "lxml")

        # product = soup5.find("h1", attrs={'class': 'proName'}).text.strip()
        # brand = soup5.find("a", attrs={'style': 'text-decoration: underline; color:#EA222F'}).text
        # price = soup5.find("div",class_ = "unf-p-summary-price").text+ " TL"
        # print("Fiyat:" + price, "Marka:" + brand, properties)
        urun.append(soup5.find("h1", attrs={'class': 'proName'}).text.strip())
        marka.append(soup5.find("a", attrs={'style': 'text-decoration: underline; color:#EA222F'}).text)
        fiyat.append(soup5.find("div", class_="unf-p-summary-price").text + " TL")
        puan.append(soup5.find("div", class_="proRatingHolder").find('strong').text)

        teknik_ayrıntılar = soup5.find_all("li", attrs={"class": "unf-prop-list-item"})
        string = ""
        for i in teknik_ayrıntılar:
            etiket = i.find("p", attrs={"class": "unf-prop-list-title"}).text
            deger = i.find("p", attrs={"class": "unf-prop-list-prop"}).text
            string = etiket + ":" + deger + ";"
            # print(string)
            a = string.rfind("Bellek Kapasitesi")
            if (a >= 0):
                # print(a)
                c = string.find(";")
                ram.append(string[a + 19:a + c])
                # print(ram)
            a = string.rfind("İşletim Sistemi:")
            if (a >= 0):
                # print(a)
                c = string.find(";")
                isletimsistemi.append(string[a + 16:a + c])
                # print(isletimsistemi)

            a = string.rfind("İşlemci:")
            if (a >= 0):
                # print(a)
                c = string.find(";")
                islemcitipi.append(string[a + 8:a + c])
                # print(islemcitipi)

            a = string.rfind("Disk Kapasitesi:")
            if (a >= 0):
                # print(a)
                c = string.find(";")
                diskboyutu.append(string[a + 16:a + c])
                # print(diskboyutu)

            a = string.rfind("Ekran Kartı Türü:")
            if (a >= 0):
                # print(a)
                c = string.find(";")
                ekrankartitipi.append(string[a + 17:a + c])
                # print(ekrankartitipi)

            a = string.rfind("Ekran Çözünürlüğü:")
            if (a >= 0):
                # print(a)
                c = string.find(";")
                ekrancozunurluk.append(string[a + 18:a + c])
                # print(ekrancozunurluk)

books_dict = {}
for i in range(0, len(urun)):
        books_dict = {"Ürün": [urun[i]]}
        # print(books_dict)
        mycol.insert_one(books_dict)

for i in range(0, len(marka)):
        books_dict = {"marka": [marka[i]]}
        # print(books_dict)
        mycol1.insert_one(books_dict)

for i in range(0, len(ram)):
        books_dict = {"ram": [ram[i]]}
        # print(books_dict)
        mycol2.insert_one(books_dict)

for i in range(0, len(isletimsistemi)):
        books_dict = {"işletim sistemi": [isletimsistemi[i]]}
        # print(books_dict)
        mycol3.insert_one(books_dict)

for i in range(0, len(islemcitipi)):
        books_dict = {"işlemci tipi": [islemcitipi[i]]}
        # print(books_dict)
        mycol4.insert_one(books_dict)

for i in range(0, len(diskboyutu)):
        books_dict = {"disk boyutu": [diskboyutu[i]]}
        # print(books_dict)
        mycol5.insert_one(books_dict)

for i in range(0, len(ekrankartitipi)):
        books_dict = {"ekran kartı tipi": [ekrankartitipi[i]]}
        # print(books_dict)
        mycol6.insert_one(books_dict)

for i in range(0, len(ekrancozunurluk)):
        books_dict = {"ekran çözünürlüğü": [ekrancozunurluk[i]]}
        # print(books_dict)
        mycol7.insert_one(books_dict)

for i in range(0, len(fiyat)):
        books_dict = {"fiyat": [fiyat[i]]}
        # print(books_dict)
        mycol8.insert_one(books_dict)

for i in range(0, len(puan)):
        books_dict = {"puan": [puan[i]]}
        # print(books_dict)
        mycol9.insert_one(books_dict)

############################################################################################################################




