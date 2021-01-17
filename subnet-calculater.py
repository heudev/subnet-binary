import os
import ipaddress
import time
#print(ipaddress.IPv4Address('192.168.1.1') + 3)
#print(ipaddress.IPv4Network('192.186.1.0/24')[127])
#net = ipaddress.IPv4Network("192.168.1.0/24")
#print(net.netmask)
#print(net.broadcast_address)

def decimal():
        print("---------------------DECIMAL TO BINARY DÖNÜŞTÜME---------------------")
        print("'1'ile'255' arası sayı giriniz.")
        try:
            a = int(input("-Sayı Giriniz: "))
        except ValueError:
            os.system("cls")
            return decimal()
        bnr = bin(a).replace('0b','')
        x = bnr[::-1]
        while len(x) < 8:
            x += '0'
        bnr = x[::-1]
        print(bnr) 
        print("")
        next2 = input("Yeniden hesaplamak için enter'a basınız, Anamenüye dönmek için 'back', çıkmak için 'exit' yazınız.: ")
        os.system("cls")
        if next2 == "":
            decimal()
        elif next2 == "back":
            anamenu()
        elif next2 == "exit":
            os.system("cls")
            print("Good Bye")
            time.sleep(1)
            os.system("exit")
        else:
            print("Yanlış değer girdiniz, lütfen bekleyiniz...")
            time.sleep(1.5)
            os.system("cls")
            return decimal()
            
def adetx():
    adet = input("Kaç subnete bölünsün: ")
    if adet == "1":
        return 0
    elif adet == "2":
        return 1
    elif adet == "4":
        return 2
    elif adet == "8":
        return 3
    elif adet == "16":
        return 4
    elif adet == "32":
        return 5
    elif adet == "64":
        return 6
    else:
        print("Yanlış değer girdiniz lütfen '1,2,4,8,16,32,64' değerlerinden birini giriniz.") 
        return adetx()
os.system("cls")
def subnet():
    print("---------------------SUBNET HESAPLAMA---------------------")
    print("--------------------------")
    print("Örnek Kullanım: \n Network Id: 192.168.1.0/24 \n Subnet Sayısı: 2" )
    print("--------------------------")
    #net = ipaddress.IPv4Network("192.168.1.0/24")
    try:
        net = ipaddress.IPv4Network(input("Network id: "))
    except:
        print("Yanlış değer girdiniz, lütfen bekleyiniz...")
        time.sleep(1.5)
        os.system("cls")
        return subnet()
    sayilar = 1
    for sn in net.subnets(adetx()):
        print("")
        print("--------Network {}--------".format(sayilar))
        print("Network id:",sn[0])
        print("Gateway:",sn[0]+1)
        print("Broadcast:",sn.broadcast_address)
        print("Subnet Mask:",sn.netmask)
        print("Kullanılabilir ip'ler:",sn[0]+1," - ",sn.broadcast_address-1)
        sayilar += 1
    print("_________________________________________________________________________________")
    print("")
    next = input("Yeniden hesaplamak için enter'a basınız, ana menüye dönmek için 'back', çıkmak için 'exit' yazınız.: ")
    os.system("cls")
    if next == "":
        subnet()
    elif next == "back":
        anamenu()
    elif next == "exit":
        os.system("cls")
        print("Good Bye")
        time.sleep(1)
        os.system("exit")
    else:
        os.system("exit")

def anamenu():
    print("-Geliştirici: @D1STANG3R")
    print("---------------------PROGRAMA HOŞGELDİNİZ---------------------")
    print("-Decimal to Binary hesaplaması için '1' yazınız...")
    print("-Subnet hesaplaması için '2' yazınız...")
    secim = input("-Seçiniz: ")
    os.system("cls")
    if secim == "1":
        decimal()
    elif secim == "2":
        subnet()
    elif secim == "exit":
        os.system("cls")
        print("Good Bye")
        time.sleep(1)
        os.system("exit")
    else:
        print("Yanlış değer girdiniz, lütfen bekleyiniz...")
        time.sleep(1)
        os.system("cls")
        return anamenu() 
anamenu()