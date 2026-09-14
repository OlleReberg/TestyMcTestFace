class Elev:
    def __init__(self, name,lastname,age,program):
        self.name = name
        self.lastname=lastname
        self.age = age
        self.program = program

    def elev_info(self):
        print("Hej, ",self.name)
        print("Du är", self.age, "gammal")
        print("Du läser", self.program+"program")

name=input("Vad heter du?: ")
lastname=input("Vad heter du i efternamn?: ")
age=int(input("Hur gammal är du?: "))
program=input("Vilket program läser du?: ")

elev1=Elev(name,lastname,age,program)
print(elev1.name)
print(elev1.lastname)
print(elev1.age)
print(elev1.program)

elev1.elev_info()