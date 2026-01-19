
# Vypracoval: Tomáš Hujíček
# Projekt: Logická hra Bulls and Cows

import random

# --- Inicializace hry a generování čísla ---

# Seznam všech možných číslic
možnosti = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
random.shuffle(možnosti)

# Na první pozicinesmí být nula
if možnosti[0] == "0":
    vyber = možnosti[1:5]
else:
    vyber = možnosti[0:4]

# Převede vybrané číslice na jeden text
tajne_cislo = "".join(vyber)

print("Vítej ve hře! Zkus uhodnout moje číslo.")
print("=" * 45)
print("Číslo je čtyřmístné a cifry se v něm neopakují.")
print("=" * 45)

pokusy = 0

# --- Hlavní část programu ---

while True:
    tip = input("Tvůj odhad: ")

    if not tip.isdigit():
        print("Můžeš zadávat jenom čísla!")
        continue

    if len(tip) != 4:
        print("Tvoje číslo musí mít přesně 4 znaky!")
        continue

    if tip[0] == "0":
        print("První cifra nesmí být nula!")
        continue

    # Kontrola duplicitních číslic pomocí setu
    if len(set(tip)) != 4:
        print("Číslice se nesmí opakovat!")
        continue

    pokusy += 1

    # Kontrola, jestli hráč vyhrál
    if tip == tajne_cislo:
        print(f"Super! Uhodl jsi to! Stačilo ti na to {pokusy} pokusů.")

        # Slovní hodnocení výkonu
        if pokusy <= 10:
            print("To je fakt parádní výsledek!")
        elif pokusy <= 20:
            print("Docela dobrý, takový průměr.")
        else:
            print("Trvalo ti to dost dlouho, ale nakonec jsi to dal.")
        break

    # Výpočet Bulls a Cows
    pocet_bulls = 0
    pocet_cows = 0

    # kontrola tipu
    for i in range(4):
        if tip[i] == tajne_cislo[i]:
            pocet_bulls += 1
        elif tip[i] in tajne_cislo:
            pocet_cows += 1

    # Výpis aktuálního stavu kola
    # Gramatika pro množné číslo
    b_text = "bull" if pocet_bulls == 1 else "bulls"
    c_text = "cow" if pocet_cows == 1 else "cows"

    print(f"Aktuálně: {pocet_bulls} {b_text}, {pocet_cows} {c_text}")
    print("-" * 45)
