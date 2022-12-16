import os
import datetime

#os.chdir(r"C:\Users\aurel\Desktop")
#print(os.getcwd())

# Kompiuterio darbalaukyje (Desktop) sukurtų katalogą „Naujas Katalogas“
#os.mkdir("Naujas_katalogas")

# Šiame kataloge sukurtų tekstinį failą, kuriame būtų šiandienos data ir laikas
#os.chdir(r"C:\Users\aurel\Desktop\Naujas_katalogas")
#print(os.getcwd())

with open("data_ir_laikas.txt", "w") as katalogas:
    katalogas.write(str(datetime.datetime.today()))

# Atspausdintų šio tekstinio failo sukūrimo datą ir dydį baitais
# Patarimai: failo sukūrimo datą galima pasiekti per os.stat(„Failas.txt“).st_size

koks_failo_dydis = os.stat("data_ir_laikas.txt").st_size
print(f"Failo dydis: {koks_failo_dydis}")
