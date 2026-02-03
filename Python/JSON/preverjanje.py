#Naloga 1
odgovor = {
    "temperatura": 24,
    "vlaznost": 60,
    "veter": 8,
    "lokacija": "Ljubljana"
}

#1.a) Izpiši temperaturo.
print(odgovor["temperatura"])

#1.b) Izpiši vlažnost.
print(odgovor["vlaznost"])

#1.c) Izpiši stavek: ”V mestu Ljubljana je 24 stopinj”.
print(f"V mestu Ljubljana je {odgovor["temperatura"]} stopinj.")

#Naloga 2
student = {
    "ime": "Marko",
    "priimek": "Horvat",
    "naslov": {
        "ulica": "Slovenska cesta 12",
        "mesto": "Maribor",
        "posta": 2000
    }
}


#2. a) Izpiši ulico.
print(student["naslov"]["ulica"])

#2. b) Izpiši priimek študenta.
print(student["priimek"])

#2.c) Izpiši stavek: ”Marko Horvat, Slovenska cesta 12”.
print(f"{student['ime']} {student['priimek']}, {student["naslov"]["ulica"]}")

#Naloga 3
razred = {
    "oznaka": "4.a",
    "dijaki": ["Ana", "Bojan", "Cvetka", "David"],
    "ocene": [5, 4, 5, 3]
}

#3 a) Izpiši prvega dijaka
print(razred["dijaki"][0])

#3 b) Izpiši tretjo oceno.
print(razred["ocene"][2])

#3 c) Izpiši VSE dijake (vsak v novi vrstici).
for dijak in razred["dijaki"]:
    print(dijak,"\n")

#Naloga 4
knjige = {
    "knjiznica": "Mestna knjiznica",
    "seznam": [
        {"naslov": "Python programiranje", "cena": 29.99},
        {"naslov": "Uvod v algoritme", "cena": 35.50},
        {"naslov": "Spletne aplikacije", "cena": 42.00}
    ]
}

#4 a) Izpiši naslov prve knjige
print(knjige["seznam"][0]["naslov"])

#4 b) Izpiši ceno druge knjige.
print(knjige["seznam"][1]["cena"])

#4 c) Za VSE knjige izpiši naslov in ceno (format: ”Python programiranje: 29.99€”).
for knjiga in knjige["seznam"]:
    print(f"{knjiga["naslov"]}: {knjiga["cena"]}€")

#Naloga 5
naročilo = {
  "id": "ORD-2024-001",
  "kupec": {
    "ime": "Petra Novak",
    "email": "petra@email.si"
  },
  "artikli": [
    { "naziv": "Miska", "kolicina": 2, "cena": 15.99 },
    { "naziv": "Tipkovnica", "kolicina": 1, "cena": 45.0 }
  ],
  "status": "potrjeno"
}

#5 a) Izpiši ID naročila
print(naročilo["id"])

#5 b) Izpiši email kupca.
print(naročilo["kupec"]["email"])

#5 c) Izpiši naziv prvega artikla.
print(naročilo["artikli"][0]["naziv"])

#5 d) Izpiši VSE artikle s količino (format: ”Miška: 2 kos/i”)
for aritekel in naročilo["artikli"]:
    print(f"{aritekel["naziv"]}: {aritekel["kolicina"]} kos/i") 

#BONUS Za naročilo iz naloge 5 izračunaj in izpiši skupno ceno vseh artiklov (cena × količnik za vsak artikel, nato seštej)
skupna = 0
for aritekel in naročilo["artikli"]:
    skupna = skupna + (aritekel["cena"] * aritekel["kolicina"])
print(f"Cena vseh artiklev je: {skupna}€")