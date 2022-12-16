# Leistų vartotojui įvesti norimą eilučių kiekį
# Leistų vartotojui įrašyti norimą kuriamo failo pavadinimą
# Įrašytų įvestą tekstą atskiromis eilutėmis į failą
#
# Sukurti while ciklą, kuris užsibaigtų tik įvedus vartotojui tuščią eilutę (nuspaudus ENTER)

eilutes = ""

while True:
    pirmas = input("Įveskite norimą tekstą: ")
    if pirmas != "":
        eilutes += pirmas + "\n"
    else:
        break

koks_pavadinimas = input("Įveskite norimą pavadinimą: ")

with open(koks_pavadinimas + ".txt", "w", encoding="UTF-8") as file:
    file.write(eilutes)