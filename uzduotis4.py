# minibiudžeto programą, kuri:
#
# Leistų vartotojui įvesti pajamas arba išlaidas (su "-" ženklu)
# Pajamas ir išlaidas saugotų sąraše, o sąrašą pickle faile (uždarius programą, įvesti duomenys nedingtų)
# Atvaizduotų jau įvestas pajamas ir išlaidas
# Atvaizduotų įvestų pajamų ir išlaidų balansą (sudėtų visas pajamas ir išlaidas)

def nuskaitymas_is_failo():
    pass
def irasyti(skaiciai):
    pass

knyga = []
zurnalas = nuskaitymas_is_failo()

while True:
    veiksmas = eval(input("""
    1 - įvesti pajamas/išlaidas
    2 - parodyti pajamas/išlaidas
    3 - balansas
    0 - išeiti
    """))


    match veiksmas:
        case 1:
            suma = eval(input("Įveskite sumą: "))
            knyga.append(suma)
            irasyti(knyga)
        case 2:
            print(knyga)
        case 3:
            print("Balansas yra: ", sum(knyga))
        case 0:
            print("Viso gero")
        case _:
            print("Neteisingas įvestas veiksmas")

