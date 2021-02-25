class Qlassy:
    def __init__(self,name,age,dob,id_number):
        self.citizenname = name
        self.ageofpeople = age
        self.dob1 = dob
        self.idn = id_number
        
    def adcit(self):
        print("Namey - " + self.citizenname)
        print("Agey - " + str(self.ageofpeople))
        print("Doby - " + self.dob1)
        print("Idy - " + str(self.idn))
        print("Citizen Added")
        
    def pointy(self):
        year = 2021 - self.idn
        print("THis Book Was published " + str(year))
        

citizen1 = Qlassy("Wompy Kid","Wompy kid i dont know","What is This",700)
citizen1.adcit()
citizen1.pointy()
citizen2 = Qlassy("Harry Potter","Potter Harry","Hprry patter",1983)
citizen2.adcit()
citizen2.pointy()
