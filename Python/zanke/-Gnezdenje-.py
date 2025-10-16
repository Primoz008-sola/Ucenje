for i in range(3):
    for j in range(3):
        print(f"({i}, {j})")

# Dodatno:
# For zanke so običajno hitrejše in bolj berljive od while zank za iteracijo čez znana zaporedja.
# While zanke so koristne, ko ne vemo vnaprej, kolikokrat se bo zanka izvedla.
# Izogibajte se neskončnim zankam (razen če so namerne).
# Uporabite enumerate(), ko potrebujete tako indeks kot vrednost elementa.
# List comprehension je pogosto hitrejši od enakovredne for zanke.

# Omejitve:
# Spreminjanje zaporedja med iteracijo lahko povzroči nepričakovane rezultate.
# Previdno pri uporabi float vrednosti v pogojih while zank zaradi možnih napak pri zaokroževanju.

