""" a,b,c = "Ana", "Peter", "Domen"
print(a,b,c,sep=" NO NO !!!  ")

 with open("test.txt", "w") as f:
    print("To bo zapisano v datoteko.", file=f)
    print("Še ena vrstica v datoteki.", file=f)


f = open("test.txt", "r")
print(f.read())
def uporabi_funkcijo(func, število):
    return func(število)

def podvoji(x):
    return x * 2

def kvadriraj(x):
    return x ** 2

print(uporabi_funkcijo(podvoji, 5))   # Izpiše: 10
print(uporabi_funkcijo(kvadriraj, 5)) # Izpiše: 25

kratko = lambda a,b:a + b
print(kratko(2,3))

sez = list("Peter")
print(sez)
sez = "".join(sez)
print(sez)

for število in [1, 2, 3, 4, 5]:
    print(število,end=";")
print() """

#0. OSNOVA naveden izpis (uporablaj tudi pri razhroščevanju), več izpisov na enkart + različni tipi podtakov (int, strg,...)
print("test")
print(""" test
      test
      test""")

# 0.1 DODATNI PARAMETRI
#1. sep (privzeto je presledek)
print("Jabolka", "Hruške", "Banane", sep=" | ")
#2 end
print("Ena", end=" ")

# 0.2 POSEBNI znaki
print("Vrstica 1\nVrstica 2")
print("Tabulatorski\tpresledek")
print("Narekovaji: \"znotraj niza\"")

#1. FORMATIRANJE
ime = "Maja"
starost = 30
print(f"{ime} je stara {starost} let.") # f-strings (Python 3.6+)
print("{} je stara {} let.".format(ime, starost)) # .format() metoda
print("%s je stara %d let." % (ime, starost)) # % operator (starejši način)

#2. DADOTEKE
with open("test.txt", "w") as f:
    print("To bo zapisano v datoteko.", file=f)
    print("Še ena vrstica v datoteki.", file=f)
