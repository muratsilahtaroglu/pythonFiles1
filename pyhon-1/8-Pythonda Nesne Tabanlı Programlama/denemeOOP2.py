def multipleinput(*args):
    talebeler=[]
    for talebe in args:
        talebeler.append(input(talebe))
    return tuple(talebeler)
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

class Talebe(Person):
    def __init__(self,name,age,departmant="Bilinmiyor"):
        super().__init__(name,age)
        self.departmant=departmant
    def __str__(self):
        return self.name
    
class Vakif(Person):
    def __init__(self,name,age,tecrube=0):
        Person.__init__(self,name,age)# or super().__init__(name,age)
        self.tecrube=tecrube
    def __str__(self):
        return self.name

class Dershane:
    Name=" "
    def __init__(self,Mudebbir:Vakif):
        self.mudebbir=Mudebbir
        self.talebeler=[]
    def TalebeEkleme(self,talebe:Talebe):
        self.talebeler.append(talebe)
    def TalelebeCikarma(self,talebe:Talebe):
        self.talebeler.remove(talebe)
    def __str__(self):
        metin=f"Dershane adı:{self.Name}\tVakıf adı:{self.mudebbir}\tDershanedeki Talebeler:"
        for talebe in self.talebeler:
            metin+=f"\n\t\t\t{talebe} age:{str(talebe.age)} bölüm:{talebe.departmant}"
        return metin

vakif=Vakif("Mehmet",40,18)
n=int(input("Talebe Sayisi:"))
CalisanDershanesi=Dershane(vakif)

for talebe in range(n):
    ad,yas,bolum=multipleinput("Talebe Adı:","Talebe Yaşı:","Talebe Bolumu:")
    CalisanDershanesi.TalebeEkleme(Talebe(ad,int(yas),bolum))
CalisanDershanesi.Name="Calisan Dershanesi"

print(CalisanDershanesi)
