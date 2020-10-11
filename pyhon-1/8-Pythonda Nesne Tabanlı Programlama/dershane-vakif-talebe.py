def multipleinput(*args):#çoklu input fonksiyonu
    y =[]
    for x in args:
        y.append(input(x))
    return tuple(y)

class Person:
        def __init__(self,name,yas):
            self.name=name
            self.yas=yas

class Talebe(Person):

    def __init__(self,name,yas,bolum="Bilinmiyor"):

        super().__init__(name,yas)
        self.bolum=bolum
    def __str__(self):
        return self.name

class Vakif(Person):

    def __init__(self,name,yas,tecrube=0):
        super().__init__(name,yas)
        self.tecrube=tecrube
    def __str__(self):
        return self.name

class Dershane:
    dershane_name=" "
    def __init__(self,Mudebbir:Vakif):
        self.mudebbir=Mudebbir
        self.talebeler=[]

    def talebe_ekle(self, talebe: Talebe):
        self.talebeler.append(talebe)
    def talebe_cikar(self,talebe):
        self.talebeler.remove(talebe)
    def __str__(self):
        metin = f"Dershane Adı:{self.dershane_name}\tVakıf Adı:{self.mudebbir}\nTalebeler:"
        for talebe in self.talebeler:
            metin+= "\n\t"+str(talebe)+" yas:"+str(talebe.yas)
        return metin

n=int(input("Dershane Talebe Sayısı:"))
v1=Vakif("İmran",29,3)
calisan_dershanesi=Dershane(v1)

for talebe in range(n):
    ad, yas, bolum=multipleinput("Talebe ismi:","Talebe Yaşı:","Talebe Bölümü:")
    calisan_dershanesi.talebe_ekle(Talebe(ad,int(yas),bolum))

calisan_dershanesi.dershane_name="Çalışan Dershanesi"


print(calisan_dershanesi)# or print(Dershane.__str__(calisan_dershanesi))

