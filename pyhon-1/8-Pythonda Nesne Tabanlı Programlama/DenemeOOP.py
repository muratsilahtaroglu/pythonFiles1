import datetime
class friends:
    #atributes
    hometown="No Informatıon"
    def __init__(self,name,birthyear,job,hometown):
        self.name=name
        self.birthyear=birthyear
        self.job=job
        self.hometown=hometown

    def age(self):
        Now=datetime.datetime.now().date()
        birtyear=self.birthyear.split("-")
        DatetimeBirtday=datetime.date(int(birtyear[0]),int(birtyear[1]),int(birtyear[2]))

        Age=Now-DatetimeBirtday
        return self.CalculateAge(Age.days)

    def CalculateAge(self,Agedays):
        self.Years=0
        self.Mounts=0
        self.Days=0

        while Agedays!=0:
            if Agedays<=30:
                self.Days=Agedays
                Agedays=0
            elif Agedays<=365:
                self.Mounts=Agedays//30
                Agedays=Agedays-self.Mounts*30
            elif Agedays>365:
                self.Years=Agedays//365
                Agedays-=self.Years*365

        return self.Years,self.Mounts,self.Days
    def __str__(self):
        print(f"{self.hometown}'li {self.name} {self.age()} yaşındadır ve bir {self.job}dir")

dict={"friend1":"\"Erhan\"\"1997-03-03\"\"Esnaf\"\"Mutki\"",
      "friend2":"\"Murat\"\"1995-07-15\"\"EEM_Engineer\"\"Bitlis\"",
      }

def start():
    try:
        for x in range(1,len(dict)+1):
            Idintifier=dict[f"friend{x}"].split("\"")
            Idintifier=[i for i in Idintifier if i!=""]
            friend=friends(Idintifier[0],Idintifier[1],Idintifier[2],Idintifier[3])
            friend.__str__()
    except Exception as e:
        print(f"Error{str(e)}")
start()

