import datetime

eilerastis = '''
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''

# 1.1. Sukurtų failą „Tekstas.txt“ su pilnu tekstu, gauto python kode paleidus „import this“.
# 1.2. Atspausdintų tekstą iš sukurto failo
with open("tekstas.txt", "w") as file:
    file.write(eilerastis)

with open("tekstas.txt", "r") as file:
    print(file.read())

# 1.3. Paskutinėje sukurto failo eilutėje pridėtų šiandienos datą ir laiką+
with open("tekstas.txt", "a") as file:
    file.write(str(datetime.datetime.today()))

# 1.4. Sunumeruotų teksto eilutes (kiekvienos pradžioje pridėtų skaičių).+

numeracija = ""
    #skaicius = 1
with open("tekstas.txt", "r") as file:
    for number, row in enumerate(file, 1):
        numeracija += f"{number} {row}"

print(numeracija)

# 1.5. Sukurtame faile eilutę "Beautiful is better than ugly."
# pakeistų į "Gražu yra geriau nei bjauru."

keiciamas = ""

with open("tekstas.txt", "r") as file:
    keiciamas = file.read()

keiciamas = keiciamas.replace("Beautiful is better than ugly.", "Gražu yra geriau nei bjauru.")

with open("tekstas.txt", "w", encoding="UTF-8") as file:
    file.write(keiciamas)

#1.6 Atspausdintų visą failo tekstą atbulai

with open("tekstas.txt", "r") as file:
    print(file.read()[::-1])

#1.7. Atspausdintų, kiek failo tekste
# yra žodžių, skaičių, didžiųjų ir mažųjų raidžių.

with open("tekstas.txt", "r") as file:
    zodz_raid_sk = file.read()

kiek_zodziu = len(zodz_raid_sk.split())
kiek_didziuju = sum(x.isupper() for x in zodz_raid_sk)
kiek_mazuju = sum(x.islower() for x in zodz_raid_sk)
kiek_skaiciu = sum(x.isnumeric() for x in zodz_raid_sk)
print(f"1.7. Žodžiai: {kiek_zodziu}, \n     Didžiosios raidės: {kiek_didziuju}, \n     Mažosios raidės: {kiek_mazuju}, \n     Skaičių yra: {kiek_skaiciu}.")

#1.8. Nukopijuotų visą sukurto failą tekstą į naują failą, tik DIDŽIOSIOMIS RAIDĖMIS
with open ("tekstas.txt", "r") as skaitomas:
    with open("dideles_raides.txt", "w") as naujas:
        naujas.write(skaitomas.read().upper())
