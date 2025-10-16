# 1.1 Operacije:
# Indeksiranje: a[0], a[-1]
# Rezine: a[1:4]
# Konkatenacija: +
# Ponavljanje: *

# 1.2 Metode: .append(), .extend(), .insert(), .remove(), .pop(), .sort()
# Preveri še vse metode seznama: Metode seznama

# 2. Dodatno:
# Seznami so spremenljivi (mutable).
# Funkcija len(a) vrne število elementov v seznamu.
# Seznam lahko vsebuje elemente različnih tipov, vključno z drugimi seznami.

# 3. Omejitve:
# Indeksi morajo biti celoštevilski.

#USTVARI SEZNAM
# Prazen seznam
prazen = []
# Seznam s elementi
stevila = [1, 2, 3, 4, 5]
# Seznam z mešanimi tipi
mesani = [1, "dva", 3.0, [4, 5]]
# Ustvarjanje s funkcijo list()
beseda = list("Python")  # ['P', 'y', 't', 'h', 'o', 'n']
# List comprehension -- MENI NOVO !!! # hitrejši od for zanke
kvadrati = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16] 
# Množenje seznama -- EMNI NOVO !!!
ponovitve = [0] * 5  # [0, 0, 0, 0, 0]


"""Dostop do elementov in rezine (slice)
Python omogoča fleksibilen dostop do elementov seznama. Vsa ideja rezin deluje tudi na stringih! Primeri:"""
seznam = [10, 20, 30, 40, 50]
# Dostop do posameznih elementov
prvi = seznam[0]  # 10
zadnji = seznam[-1]  # 50
# Rezine
prvih_trije = seznam[:3]  # [10, 20, 30]
zadnji_trije = seznam[-3:]  # [30, 40, 50]
vsak_drugi = seznam[::2]  # [10, 30, 50]
# Obrnjen seznam
obrnjeno = seznam[::-1]  # [50, 40, 30, 20, 10]
# Kopiranje seznama
kopija = seznam[:]

# Operacije:
# Indeksiranje (pozitivno in negativno)
# Rezine z začetnim indeksom, končnim indeksom in korakom
# Obračanje seznama
# Plitko kopiranje seznama

# Dodatno:
# Negativni indeksi štejejo od konca seznama.
# Rezine ustvarijo nov seznam (kopijo).
# Korak v slicu lahko uporabimo za preskakovanje elementov ali obračanje seznama.

# Omejitve:
# Dostop do neobstoječega indeksa povzroči IndexError. Kako mimo njega?

a = [1, 2, 3]
b = [4, 5, 6]
# Združevanje seznamov
c = a + b  # [1, 2, 3, 4, 5, 6]
# Ponavljanje seznama
ponovljen = a * 3  # [1, 2, 3, 1, 2, 3, 1, 2, 3]
# Dolžina seznama
dolzina = len(a)  # 3
# Iskanje
indeks = a.index(2)  # 1
stevilo_trojk = a.count(3)  # 1
# Sortiranje
a.sort()  # Sortira seznam na mestu (destruktivno)
sortirano = sorted(b)  # Vrne nov sortiran seznam
# Obračanje
a.reverse()  # Obrne seznam na mestu
# Čiščenje seznama
a.clear()  # Odstrani vse elemente

#NAPREDNO sam ne...