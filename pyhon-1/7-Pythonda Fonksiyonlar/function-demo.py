# 1- Gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazın. 

# def yazdir(kelime, adet):
#     print(kelime * adet)

# yazdir('Merhaba\n', 10)


# 2- Kendine gönderilen sınırsız sayıdaki parametreyi bir listeye çeviren fonksiyonu yazınız.

def listeyeCevir(*params):
    liste = []

    for param in params: # yada liste=list(params)
        liste.append(param)

    return liste

result = listeyeCevir(10,20,30,'Merhaba')

print(result)


# 3- Gönderilen 2 sayı arasındaki tüm asal sayıları bulun.

# def asalSayılariBul(sayi1, sayi2):
#     for sayi in range(sayi1, sayi2+1):
#         if sayi > 1:
#             for i in range(2, sayi):
#                 if (sayi % i == 0):
#                     break
#                 else:
#                     print(sayi)

# sayi1 = int(input('sayı 1:'))
# sayi2 = int(input('sayı 2:'))
# asalSayılariBul(sayi1, sayi2)

#3.2 alternatif cevap
# def asalsayibulma(sayi1,sayi2):
#     liste=[]
#     if sayi1<2:
#         sayi1=2
#     if sayi1>sayi2:
#         sayi1,sayi2=sayi2,sayi1
#     while sayi1<sayi2:
#         asalMi= True
#         i=1
#         while i<sayi1/2:
#             i+=1
#             if sayi1%i==0:
#                 asalMi=False
#                 break
#
#         if asalMi==True:
#             liste.append(sayi1)
#
#         sayi1+=1
#     return liste
# # print(asalsayibulma(int(input("Sayi1:")),int(input("Sayi2:"))))

# 4- Kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndürünüz.


def tamBolenleriBul(sayi):
    tamBolenler = []

    for i in range(2, sayi):
        if (sayi % i == 0):
            tamBolenler.append(i)
    
    return tamBolenler
def tamB(sayi):
    tamBolen= [i for i in range(2,sayi) if (sayi%i==0) ]
    print(f"TamBolenler:{tamBolen}")
sayi=int(input("Sayi:"))
print(tamBolenleriBul(sayi))
tamB(sayi)
