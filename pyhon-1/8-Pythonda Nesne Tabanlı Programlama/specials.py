mylist = [1,2,3]
# myString = 'my string'

# print(len(mylist))
# print(len(myString))
# print(type(mylist))
# print(type(myString))

class Movie():
    def __init__(self, title, director, duration):
        self.title = title
        self.director = director
        self.duration = duration
        print('movie objesi oluşturuldu.')

    def __str__(self):
        return f"{self.title} by {self.director}"

    def __len__(self):
        return self.duration
    
    def __del__(self):
        print('film objesi silindi')

m = Movie('film adı','yönetmen adı',120)
print(m)# yada print(m) --> istenilen ifadey __str__ ifadesinin altından döndürülür
# del m #--> print(m) # bu çalştırılınca m objesini siler ve yukardaki __del__ nin altıbdaki print ifadesi çalışır

print("len:",len(m))# normalde len komutu çalışmaz çalışması için bu komut kullanılabilir. ve istenilen ifade return edilebilir

