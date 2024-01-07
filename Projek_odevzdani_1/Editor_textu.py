'''
author =
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
password = {user_1["heslo"]:user_1,
            user_2["heslo"]:user_2,
            user_3["heslo"]:user_3,
            user_4["heslo"]:user_4
            }
#VYBER UZIVATELE
prihlasovaci_jmeno = "bob"
heslo = "123"
if prihlasovaci_jmeno in user and heslo in password:
    print("Zdravím mužes pokračovat dál do programu " + prihlasovaci_jmeno)
else:
    print("Zadané udaje nesouhlasí.\nUkončuji program!")
    quit()

#vyber textu
texty = ("Text 1","Text 2","Text 3")
odelovac = "=" * 60
delka_cary = len(odelovac)
print(odelovac)
print("Vytej v analyzátoru textu =)".upper().center(delka_cary))
print(odelovac)
print()
print((" / "+ " / ".join(texty)+ " / ").center(delka_cary))
print(odelovac)
vyber_textu = input("Vyber si číslo textu od 1 do 3: ")