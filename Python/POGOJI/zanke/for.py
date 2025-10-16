zaporedje = []
for element in zaporedje:
    pass
    # koda, ki se izvede za vsak element

#Napredne tehnike
#ENUMERATE
for indeks, element in enumerate(["a", "b", "c"]):
    print(f"Indeks: {indeks}, Element: {element}")

#Zip za vzporedno iteracijo:
imena = ["Ana", "Bor", "Cene"]
ocene = [5, 4, 3]
for ime, ocena in zip(imena, ocene):
    print(f"{ime} ima oceno {ocena}")

# List comprehension (seznam razumevanje):
kvadrati = [x**2 for x in range(10)]