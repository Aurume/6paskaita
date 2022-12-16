# Leistų vartotojui įvesti norimą eilučių kiekį
# Leistų vartotojui įrašyti norimą kuriamo failo pavadinimą
# Įrašytų įvestą tekstą atskiromis eilutėmis į failą
# Patarimai:
#
# Sukurti while ciklą, kuris užsibaigtų tik įvedus vartotojui tuščią eilutę (nuspaudus ENTER)
tekstas = ""

while True:
    pirmas = input("Įveskite eilutę: ")
    if pirmas != "":
        tekstas += pirmas + "\n"
    else:
        break

failo_pavadinimas = input("Įveskite failo pavadinimą: ")

with open(failo_pavadinimas + ".txt", "w", encoding="UTF-8") as failas:
    failas.write(tekstas)