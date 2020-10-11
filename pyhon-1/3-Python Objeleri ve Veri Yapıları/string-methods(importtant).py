message = 'Hello There. My name is Sadık Turan'
message = message.split()


message = message.upper()
message = message.lower()
message = message.title()
message = message.capitalize()

message = message.strip() #baştaki  ve sondaki boşkuları siler
message = message.lstrip() #left strip
message = message.rstrip() #right strip
message = message.strip('.')#  vb strip içine ne yazsan baştaki  ve sondaki . ları siler
message = message.strip('.,! ')#  vb strip içine ne yazsan baştaki  ve sondaki . , ! leri siler
message = message.strip('Hello')#  baş ve sondaki Hello ifadelerini siler
message = message.split()# başluğa kadar olan ifadeleri diziye dönüştürür.
message = message.split('.')# . ya kadar olan ifadeleri diziye dönüştür.
message=re.split('\.|, ',message ) # birden fazla seçenek ile istenilen yerleri diziye döniştür.
# message=re.split('[.,]',message )
#re: regular expression için import re demek lazımdır. .,* gibi bazı ifadeler tanımlı olduğu için\. ve \* olarak kullanılmalıdır.
#---------------
message2=r"  C:\dosya1\dosya2; ;  C:\dosya1\dosya5\dosya3.tfddfxt; D:\dosya1\dosya3.c54dfs; D:\test.xm656l "
print([l[:l.find(".")] for l in [x.split("\\")[-1].strip(" ") for x in message.split(";")] if l != ""])
# message2 yi ['dosya', 'dosya3', 'dosya3', 'test'] ifadeye dönüştürür
# l[:l.find(".")] komutu baştan ilk noktaya kadar ki kısm alır. [] İFADELER LİSTELERİ(dizi) TUTAR
#--------------

message= '---'.join(message)

index = message.find('Sadık')# ilk Sadık ı arar ve S nin indexini döndür.
message3="I am Murat. Murat is handsome"
index = message3.find('Murat',7)# ilk 7 karakterden sonra Murat'ı arar
# message3[:message3.find(".")] baştan başlayıp karakter dizisini . ya kadar döndürür
# message3[message3.find(".")+len(".")+2:] .dan sonra +2 den başlayıp karakter dizisini sona kadar döndürür
# rfind sağdan aramaya başlar
#-----------
isFound = message.startswith('H')
isFound = message.endswith('n')

message = message.replace('Sadık','Çınar')
message = message.replace('ç','c')\
                 .replace('ö','o')\
                 .replace(' ','-')

message = message.center(50,'*')
+522
print(message)
