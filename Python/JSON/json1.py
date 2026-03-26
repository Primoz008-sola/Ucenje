student = {
"ime":"Marko",
"priimek": "Horvat",
"naslov": {
    "ulica": " Slovenska cesta 12",
    "mesto": " Maribor ",
    "posta": 2000
}
}

print(student["naslov"]["ulica"])

knjige = {
" knjiznica ": " Mestna knjiznica ",
" seznam ": [
{" naslov ": " Python programiranje ", " cena ": 29.99} ,
{" naslov ": " Uvod v algoritme ", " cena ": 35.50} ,
{" naslov ": " Spletne aplikacije ", " cena ": 42.00}
]
}
print(knjige[" seznam "][0][" naslov "])
i = 0
print("\n\n\n-------------------------------------------------------------------------------------------------\n")
for s in knjige[" seznam "]:
    #print(s[" naslov "], " - ", s[" cena "], " EUR")
    i += 1
    print(f"{i}: {s[" naslov "]} Cena:{s[" cena "]} €")