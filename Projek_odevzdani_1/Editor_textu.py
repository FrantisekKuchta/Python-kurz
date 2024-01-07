'''
projekt_1.py: první projekt do Engeto Online Python Akademie
author: František Kuchta
email: kuchta.f@seznam.cz
discord:FrantisekK #fanyny94

'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]
#uzivatele registrovaNI
user_1 = {"prihlasovaci jmeno" : "bob","heslo": "123"}
user_2 = {"prihlasovaci jmeno" : "ann","heslo": "pas123"}
user_3 = {"prihlasovaci jmeno" : "mike","heslo": "password123"}
user_4 = {"prihlasovaci jmeno" : "liz","heslo": "pass123"}
user = {user_1["prihlasovaci jmeno"]:user_1,
        user_2["prihlasovaci jmeno"]:user_2,
        user_3["prihlasovaci jmeno"]:user_3,
        user_4["prihlasovaci jmeno"]:user_4
        }
#print(user)
password = {user_1["heslo"]:user_1,
            user_2["heslo"]:user_2,
            user_3["heslo"]:user_3,
            user_4["heslo"]:user_4
            }
#VYBER UZIVATELE
prihlasovaci_jmeno = input("Zadej své přihlašovací jméno: ")
heslo = input("Zadej heslo: ")
if prihlasovaci_jmeno in user and heslo in password:
    print("Zdravím mužes pokračovat dál do programu " + prihlasovaci_jmeno)
else:
    print("Zadané udaje nesouhlasí.\nUkončuji program!")
    quit()

#vyber textu
odelovac = "=" * 60
delka_cary = len(odelovac)
print(odelovac)
print("Vytej v analyzátoru textu =)".upper().center(delka_cary))
print(odelovac)

#vyber textu

cislo_textu = input("Vyber si číslo textu od 1 do 3: ")
if cislo_textu.isalpha():
    print("Zadal jsi pismena, Ukončuji program!")
    quit()
elif 1<= int(cislo_textu) <=3 :
    vybrany_text = TEXTS[int(cislo_textu) - 1]
    #print("spravně")
else:
    print("Dané číslo neni v razsahu vyběru ukoncuji program!")
    quit()

#print(vybrany_text)

#práce s textem
    #počet slov
slova = []
for slovo in vybrany_text.split():
    slova_v_textu = slovo.strip(",.:-;!?")
    slova.append(slova_v_textu)
#print(len(slova))
#print(f"V textu je {len(slova)} slov.")

#pocet s velkymi pismeny
slova_zacatek_velkym_pismeny = []
for slovo in slova:
        if slovo.istitle():
            slova_zacatek_velkym_pismeny.append(slovo)
#print(len(slova_velkym_pismeny))
#print(str(slova_velkym_pismeny))
#pocet s malimi psiemny
slova_velka_pismena = []
for slovo in slova:
        if slovo.isupper():
            slova_velka_pismena.append(slovo)
#print(slova_velka_pismena)

slova_mala_pismena = []
for slovo in slova:
     if slovo.islower():
          slova_mala_pismena.append(slovo)
#print(slova_mala_pismena)
#print(len(slova_mala_pismena))

cisla = []
for cislo in slova:
     if cislo.isdigit():
          cisla.append(cislo)
#print(cisla)
#print(len(cisla))
total = 0
for element in cisla:
     if isinstance(element, int) or element.isdigit():
          total += int(element)
#print(total)
          
print(odelovac)
print(f"V textu je {len(slova)} slov.")
print(f"Počet slov s začínajících velkým písmenem je {len(slova_zacatek_velkym_pismeny)}")
print(f"Počet slov psaných velkým písmem je {len(slova_velka_pismena)} ")
print(f"Počet slov psaných malím písmem je {len(slova_mala_pismena)}")
print(f"Pošet cisel v textu je {len(cisla)}")
print(f"Součet vsech čísel v textu je {total}")


    



    


