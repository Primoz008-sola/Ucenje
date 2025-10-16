# 1. Operacije:
# Preverjanje enega ali več pogojev
# Izvajanje različnih blokov kode glede na pogoje
# Gnezdenje pogojev

# 2. Dodatno:

# Python uporablja zamike za določanje blokov kode. Enako pri funkcijah, objektih in zankah.
# Lahko uporabimo pass stavek za prazen blok kode.
# If preveri vse pogoje, medtem ko elif preveri samo, dokler ne najde prvega resničnega pogoja. Če je en elif resničen, ostali pogoji v verigi niso preverjeni.

# 3. Omejitve:
# Preveč gnezdenih if stavkov lahko poslabša berljivost kode.

# Kompaktna oblika if-else stavkov v eni vrstici. ....

#logični opratorji
# "short-circuit" vrednotenje
a = None
b = "Privzeto"
rezultat = a or b  # Vrne "Privzeto"

#Match stavki (Python 3.10+)
# Match s pogoji
command = "quit"
match command:
    case "quit" | "exit":
        print("Izhod iz programa")
    case "restart" if povezava_aktivna:
        print("Ponovni zagon")
    case str() as unknown_command:
        print(f"Neznani ukaz: {unknown_command}")

# Razstavljanje struktur
point = (3, 4)
match point:
    case (0, 0):
        print("Izhodišče")
    case (0, y):
        print(f"Y os, y={y}")
    case (x, 0):
        print(f"X os, x={x}")
    case (x, y):
        print(f"Točka: ({x}, {y})")
    case _:
        print("Ni točka")
