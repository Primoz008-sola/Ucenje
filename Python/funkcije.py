#1
def sestej(a, b):
    vsota = a + b
    return vsota

rezultat = sestej(5, 3)
print(rezultat)  # Izpiše: 8

# Lahko tudi direktno uporabimo:
print(sestej(10, 20))  # Izpiše: 30
#funkcije lahko kličmo tudi v drugih funkcijah

#2
def pozdravi(ime="prijatelj"):
    pass
pozdravi() #ne potrebuje vsebine

#3 lambadan funkcija
# Enaka lambda funkcija
kvadriraj_lambda = lambda x: x ** 2
print(kvadriraj_lambda(5)) # Izpiše: 25

#4 
# Funkcije lahko pošljemo kot argumente drugim funkcijam.
def uporabi_funkcijo(func, število):
    return func(število)
def podvoji(x):
    return x * 2
def kvadriraj(x):
    return x ** 2
print(uporabi_funkcijo(podvoji, 5))   # Izpiše: 10
print(uporabi_funkcijo(kvadriraj, 5)) # Izpiše: 25