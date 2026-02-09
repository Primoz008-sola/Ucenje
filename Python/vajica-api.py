import requests

url = "https://restcountries.com/v3.1/all?fields=name,borders"
odgovor = requests.get(url).json()

i = 1
max_borders = 0
for drzava in odgovor:
    print(f"{i}. {drzava["name"]["common"]}")
    stevilo_borders = len(drzava["borders"])
    print(f"{drzava.get("borders", [])})  {stevilo_borders}")
    print(f"\n{"*"*20}")
    if stevilo_borders > max_borders:
        max_borders = stevilo_borders
        borders_država = {drzava["name"]["common"]}
    i += 1
print(f"Država, ki ima največ mej je: {str(borders_država)}, ima {max_borders} sosednjih držav.")


i = 1
max_borders = 0
for drzava in odgovor:
    print(f"{i}. {drzava["name"]["common"]}")
    stevilo_borders = len(drzava["borders"])
    print(f"{drzava.get("borders", [])})  {stevilo_borders}")
    print(f"\n{"*"*20}")
    if stevilo_borders > max_borders:
        max_borders = stevilo_borders
        borders_država = {drzava["name"]["common"]}
    i += 1
print(f"Država, ki ima največ mej je: {str(borders_država)}, ima {max_borders} sosednjih držav.")
