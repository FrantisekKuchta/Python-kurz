from pprint import pprint
oddelovac = "=" * 80

sluzby = ("dostupne filmy", "detaily filmu", 'reziseri', "doporuc film")

uzivatele = {
    "tomas": {"Shawshank Redemption", "The Godfather", "The Dark Knight"},
    "petr": {"The Godfather", "The Dark Knight"},
    "marek": {"The Dark Knight", "The Prestige"}
}

film_1 = {
    "JMENO": "Shawshank Redemption",
    "HODNOCENI": "93/100",
    "ROK": 1994,
    "REZISER": "Frank Darabont",
    "STOPAZ": 144,
    "HRAJI": ("Tim Robbins", "Morgan Freeman", "Bob Gunton", "William Sadler",
      "Clancy Brown", "Gil Bellows", "Mark Rolston", "James Whitmore",
      "Jeffrey DeMunn", "Larry Brandenburg"
     )
}

film_2 = {
    "JMENO": "The Godfather",
    "HODNOCENI": "92/100",
    "ROK": 1972,
    "REZISER": "Francis Ford Coppola",
    "STOPAZ": 175,
    "HRAJI": ("Marlon Brando", "Al Pacino", "James Caan",
      "Richard S. Castellano", "Robert Duvall", "Sterling Hayden",
      "John Marley", "Richard Conte"
    )
}

film_3 = {
    "JMENO": "The Dark Knight",
    "HODNOCENI": "90/100",
    "ROK": 2008,
    "REZISER": "Christopher Nolan",
    "STOPAZ": 152,
    "HRAJI": ("Christian Bale", "Heath Ledger", "Aaron Eckhart",
      "Michael Caine", "Maggie Gyllenhaal", "Gary Oldman", "Morgan Freeman",
      "Monique Gabriela", "Ron Dean", "Cillian Murphy"
    )
}

film_4 = {
    "JMENO": "The Prestige",
    "HODNOCENI": "85/100",
    "ROK": 2006,
    "REZISER": "Christopher Nolan",
    "STOPAZ": 130,
    "HRAJI": ("Hugh Jackman", "Christian Bale", "Michael Caine",
      "Piper Perabo", "Rebecca Hall", "Scarlett Johansson", "Samantha Mahurin",
      "David Bowie"
    )
}
reziseri={film_1["REZISER"]: film_1,
          film_2["REZISER"]: film_2,
          film_3["REZISER"]: film_3,
          film_4["REZISER"]: film_4
          }

filmy={film_1["JMENO"]: film_1,
      film_2["JMENO"]: film_2,
      film_3["JMENO"]: film_3,
      film_4["JMENO"]: film_4
      }
delka_cary=len(oddelovac)
uzivatel=input("ZADEJ JMENO: ")
if uzivatel in uzivatele:
    print("V poradku")
    print(oddelovac)
    print("vitejte v nasem filmovem slovniku".upper().center(delka_cary))
    print(oddelovac)
    print((" / "+ " / ".join(sluzby)+ " / ").center(delka_cary))
else:
    print("Nejsi registrovany. Opusti stránku!")
    quit()

## Uvítání a výpis nabídky ##################################################

## Výběr služby #############################################################
vyber = input("Vyber si sluzbu: ")
if vyber in sluzby and vyber == "dostupne filmy":
    print("Dostupne filmy:\n ".upper() + " , ".join(tuple(filmy.keys())).center(delka_cary))
    print(oddelovac)

elif vyber in sluzby and vyber == "detaily filmu":
    print("Dostupne filmy:\n ".upper() + " , ".join(tuple(filmy.keys())).center(delka_cary))
    film = input("Vyber film: ")
    print(oddelovac, f"FILM: {film}", filmy.get(film), oddelovac, sep="\n")

elif vyber in sluzby and vyber == "reziseri":
    print("Reziseri: \n".upper() + " , ".join(tuple(reziseri.keys())))

else:
    print("vybrana sluzba neni v nabidce, ukoncuji..")
## Výpis všech dostupných filmů #############################################
    

## Vyber film a zobraz detaily o něm ########################################

## Vyber všechny režiséry ###################################################

## Doporuč film podle ostatních uživatelů ###################################