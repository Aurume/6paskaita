# minibiudžeto programą, kuri:
#
# Leistų vartotojui įvesti pajamas arba išlaidas (su "-" ženklu)
# Pajamas ir išlaidas saugotų sąraše, o sąrašą pickle faile (uždarius programą, įvesti duomenys nedingtų)
# Atvaizduotų jau įvestas pajamas ir išlaidas
# Atvaizduotų įvestų pajamų ir išlaidų balansą (sudėtų visas pajamas ir išlaidas)
# Patarimas: import pickle

zurnalas = []
while True:
    veiksmas = int(input("""1 - įvesti pajamas/išlaidas
    2 - parodyti pajamas/išlaidas
    3 - balansas
    0 - išeiti
    """))
    match veiksmas:
        case 1:
            suma = float(input("Įveskite sumą: "))
            zurnalas.append(suma)
        case 2:
            print(zurnalas)
        case 3:
            print("Balansas yra: ", sum(zurnalas))
        case 0:
            print("Viso gero")
        case _:
            print("Neteisingas veiksmas")

