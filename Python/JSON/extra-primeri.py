#Naloga 1: Delavnica 
# Podan je slovar omara: 
omara = { "zgornji_predal": ["žeblji", "lepilo", "trak"], 
         "spodnji_predal": [ {"orodje": "kladivo", "teza": 2}, 
                            {"orodje": "klešče", "teza": 1} ] }

#a) Izpiši niz: "lepilo" 
# Odgovor: print(omara["zgornji_predal"][1])

# b) Izpiši številko:2 
# Odgovor: print(omara["spodnji_predal"][0]["teza"]) 

# c) Izpiši niz: "klešče" Odgovor: print(omara["spodnji_predal"][1]["orodje"])

#Naloga 5: Vesoljska postaja
#Podan je slovar postaja:
postaja = {
    "moduli": [
        {"ime": "habitat", 
         "posadka": 6},
        {"ime": "laboratorij", "posadka": 2, 
         "eksperimenti": ["alge", 
                          "kristali"]}
    ],
    "sistemi": {
        "energija": {"soncne_celice": True, "napolnjenost": 78},
        "zivljenjska_podpora": {"kisik": {"status": "OK", "rezerva_ur": 48}}
    }
}


#a) Izpiši niz: "kristali"
print(postaja["moduli"][1]["eksperimenti"][1])
#b) Izpiši število članov posadke v modulu "habitat"
print(postaja["moduli"][0]["posadka"])
#c) Izpiši število ur rezerve kisika (48)
print(postaja["sistemi"]["zivljenjska_podpora"]["kisik"]["rezerva_ur"])

trgovina = {
    "promocija": {
        "akcija": 20,
        "popust": 10
    }
}

print(list(trgovina["promocija"].keys())[1])
print(trgovina["promocija"])
print(list(trgovina["promocija"])[1])