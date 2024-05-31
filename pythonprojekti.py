import random

# Pelaajan alkutiedot roolin mukaan
def initialize_player(role):
    base_player = {
        "health": 40,
        "gold": 0,
        "inventory": {
            "miekka": False,
            "kilpi": False,
            "haarniska": False,
            "saappaat": False,
            "ruokaa": 0,
            "taikajuoma": 0,
            "avain": 0
        },
        "experience": 0,
        "level": 1
    }
    if role == "velho":
        base_player["health"] = 20
        base_player["inventory"]["taikajuoma"] = 3
    elif role == "ritari":
        base_player["health"] = 40
        base_player["inventory"]["miekka"] = True
        shop_items["miekka"]["bought"] = True 
    elif role == "seikkailija":
        base_player["gold"] = 10
        base_player["inventory"]["ruokaa"] = random.randint(1,2)
        base_player["inventory"]["taikajuoma"] = random.randint(0,1)
        base_player["inventory"]["avain"] = random.randint(0,1)
    return base_player

# Pelaajan roolin valinta
def choose_role():
    roles = ["velho", "ritari", "seikkailija"]
    print("Valitse roolisi:")
    print("Roolit:\n-Velho, synnyt potioneiden kanssa\n-Ritari, syntyy miekan kanssa\n-Seikkailija. syntyy satunnaisten apuvälineiden kanssa")
    choice = input("Rooli: ").lower().strip()
    while choice not in roles:
        print("Virheellinen valinta. Yritä uudelleen.")
        choice = input("Rooli: ").lower().strip()
    return choice

# Vihollinen lista ja lore
enemies = {
    "Rotta": {"health": 5, "gold": 1, "lore": "Pieni rotta, joka etsii ruokaa.", "strength": 1},
    "Käärme": {"health": 8, "gold": 2, "lore": "Vaarallinen käärme, joka lymyilee ruohikossa.", "strength": 1},
    "Susi": {"health": 12, "gold": 4, "lore": "Nälkäinen susi, joka vaeltelee metsissä.", "strength": 2},
    "Hiisi": {"health": 15, "gold": 5, "lore": "Pieni ja viekas olento, joka rakastaa kultaa.", "strength": 2},
    "Örkki": {"health": 25, "gold": 10, "lore": "Suuri ja vahva hirviö, joka asuu luolissa.", "strength": 3},
    "Peikko": {"health": 40, "gold": 15, "lore": "Hidas mutta voimakas hirviö, joka asuu siltojen alla.", "strength": 5},
    "Kuollut ritari": {"health": 50, "gold": 30, "lore": "Muinaisen kuninkaan kirous, joka on noussut haudastaan.", "strength": 6},
    "Jättiläishämähäkki": {"health": 35, "gold": 12, "lore": "Pelottava hämähäkki, joka kutoo verkkoja metsiin.", "strength": 4},
    "Ryöväri": {"health": 20, "gold": 7, "lore": "Konna, joka ryöstää kulkijoita teiden varsilla.", "strength": 3},
    "Lohikäärme": {"health": 100, "gold": 50, "lore": "Muinaisaikojen peto, joka vartioi aarretta.", "strength": 10}
}

# Kauppa
shop_items = {
    "miekka": {"price": 5, "bought": False},
    "kilpi": {"price": 4, "bought": False},
    "haarniska": {"price": 8, "bought": False},
    "saappaat": {"price": 3, "bought": False},
    "ruokaa": {"price": 1, "bought": 0},
    "taikajuoma": {"price": 3, "bought": 0},
    "avain": {"price": 2, "bought": 0}
}

# Dungeoneita ja lore
dungeons = {
    "Hiiden Luola": {"lore": "Pimeä luola täynnä hiisiä. Kuuluu kumea kähinä.", "enemies": ["Hiisi", "Hiisi", "Örkki"]},
    "Örkki Leiri": {"lore": "Vaarallinen leiri, jossa orkit harjoittelevat taistelua.", "enemies": ["Örkki", "Örkki", "Peikko"]},
    "Muinaiset Rauniot": {"lore": "Muinaisten aikojen rauniot, joissa kummittelee.", "enemies": ["Kuollut ritari", "Peikko", "Lohikäärme"]},
    "Rosvojen Piilopaikka": {"lore": "Rosvojen piilopaikka, jossa he suunnittelevat ryöstöretkiään.", "enemies": ["Ryöväri", "Ryöväri", "Örkki"]},
    "Hämähäkin Pesä": {"lore": "Hämähäkkien pesä, joka on täynnä verkkoja ja vaaroja.", "enemies": ["Jättiläishämähäkki", "Jättiläishämähäkki", "Peikko"]}
}

# Uusia paikkoja ja tapahtumia
places = {
    "Metsä": {"lore": "Tiheä metsä, jossa voi piillä vaaroja tai aarteita.", "event": "random"},
    "Kylä": {"lore": "Rauhallinen kylä, jossa voit levätä ja käydä kaupassa.", "event": "shop"},
    "Linna": {"lore": "Vanha linna, jossa huhutaan olevan aarre.", "event": "dungeon"},
    "Järvi": {"lore": "Kaunis järvi, jonka ympärillä voi kohdata yllätyksiä.", "event": "random"},
    "Vuori": {"lore": "Korkea vuori, jossa asuu vaarallisia olentoja.", "event": "dungeon"},
    "Aavikko": {"lore": "Kuuma ja kuiva autiomaa, jossa voi kohdata vaarallisia olentoja.", "event": "random"},
    "Suo": {"lore": "Kostea ja pimeä suo, jossa piilee vaaroja.", "event": "random"}
}

def print_status():
    print(f"\nHP: {player['health']}, Kulta: {player['gold']}, Kokemus: {player['experience']}, Tasot: {player['level']}")

def level_up():
    if player["experience"] >= player["level"] * 10:
        player["level"] += 1
        player["experience"] = 0
        player["health"] = 100
        print(f"\nOnneksi olkoon! Olet noussut tasolle {player['level']} ja elämät ovat palautettu!")

def fight_enemy(enemy):
    print(f"\nLöydät hirviön: {enemy} ({enemies[enemy]['lore']}).")
    if enemies[enemy]["strength"] > 3 and not (player["inventory"]["miekka"] and player["inventory"]["kilpi"] and player["inventory"]["haarniska"]):
        print("VAROITUS: TAPPELU TÄTÄ VIHOLLISTA VASTAAN VOI KOITUA KUOLEMAKSI ilman miekkaa, kilpeä ja haarniskaa.")
    
    choice = input("Haluatko tapella tätä vihollista vastaan? KYLLÄ/EI: ").lower().strip()
    if choice == "kyllä":
        enemy_health = enemies[enemy]["health"]
        while enemy_health > 0 and player["health"] > 0:
            print_status()
            print("\nValitse toiminto: HYÖKKÄÄ/PARANNA/PAKENE")
            action = input("Toiminto: ").lower().strip()
            if action == "hyökkää":
                if player["inventory"]["miekka"]:
                    damage = random.randint(10, 20)
                else:
                    damage = random.randint(1, 10)
                enemy_health -= damage
                print(f"Teit {damage} vahinkoa {enemy}lle.")
            elif action == "paranna" and player["inventory"]["ruokaa"] > 0:
                heal = random.randint(5, 15)
                player["health"] += heal
                player["inventory"]["ruokaa"] -= 1
                print(f"Parannat itseäsi {heal} HP:llä. Sinulla on nyt {player['health']} HP.")
            elif action == "paranna" and player["inventory"]["taikajuoma"] > 0:
                heal = random.randint(10, 25)
                player["health"] += heal
                player["inventory"]["taikajuoma"] -= 1
                print(f"Käytät parannusjuoman ja parannat itseäsi {heal} HP:llä. Sinulla on nyt {player['health']} HP.")
            elif action == "pakene":
                print(f"Pakenit kauas pois ja {enemy} hukkasi sinut.")
                return
            else:
                print("Virheellinen komento tai ei riittävästi resursseja.")
            
            if enemy_health > 0:
                damage = random.randint(1, 10)
                if player["inventory"]["kilpi"]:
                    damage -= random.randint(1, 5)
                if damage < 0:
                    damage = 0
                player["health"] -= damage
                print(f"{enemy} teki {damage} vahinkoa sinulle.")
        
        if player["health"] > 0:
            print(f"Voitit {enemy}n ja sait {enemies[enemy]['gold']} kultaa sekä {enemies[enemy]['strength']} kokemuspistettä!")
            player["gold"] += enemies[enemy]["gold"]
            player["experience"] += enemies[enemy]["strength"]
            level_up()
        else:
            print(f"{enemy} voitti sinut ja kuolit... \n")
            restart_game()

def shop():
    while True:
        print(f"\nTervetuloa kauppaan! Mitä haluat ostaa? Sinulla on nyt {player['gold']} kultaa.")
        for item, info in shop_items.items():
            if item == "ruokaa" or item == "taikajuoma" or item == "avain":
                print(f"{item.upper()} {info['price']} kultaa (sinulla on {player['inventory'][item]})")
            elif not info["bought"]:
                print(f"{item.upper()} {info['price']} kultaa")
        
        print("Komento POISTU KAUPASTA")
        choice = input("Mitä haluat ostaa?: ").lower().strip()
        if choice in shop_items:
            if choice in ["ruokaa", "taikajuoma", "avain"]:
                if player["gold"] >= shop_items[choice]["price"]:
                    player["gold"] -= shop_items[choice]["price"]
                    player["inventory"][choice] += 1
                    print(f"Ostit {choice}.")
                else:
                    print("Sinulla ei ole tarpeeksi kultaa.")
            elif player["gold"] >= shop_items[choice]["price"] and not shop_items[choice]["bought"]:
                player["gold"] -= shop_items[choice]["price"]
                player["inventory"][choice] = True
                shop_items[choice]["bought"] = True
                print(f"Ostit {choice}.")
            else:
                print("Sinulla ei ole tarpeeksi kultaa tai olet jo ostanut tämän esineen.")
        elif choice == "poistu kaupasta":
            break
        else:
            print("Virheellinen valinta.")

def explore_dungeon(dungeon_name):
    dungeon = dungeons[dungeon_name]
    print(f"\n{dungeon_name} ({dungeon['lore']})")
    for enemy in dungeon["enemies"]:
        fight_enemy(enemy)
        if player["health"] <= 0:
            break

def explore_place(place):
    print(f"\nSaavut paikkaan: {place} ({places[place]['lore']})")
    event = places[place]["event"]
    if event == "shop":
        shop()
    elif event == "dungeon":
        if player["inventory"]["avain"] > 0:
            paatos = input(f"Haluatko käyttää avaimen? Sinulla on {player['inventory']['avain']}. Kyllä/ei: ")
            if paatos == 'kyllä':
                player["inventory"]["avain"] -= 1
                dungeon = random.choice(list(dungeons.keys()))
                explore_dungeon(dungeon)
            else:
                print('Et käytä avainta ja jatkat matkaa.')
        else:
            print("Sinulla ei ole avainta.")
    else:
        encounter = random.choice(list(enemies.keys()))
        fight_enemy(encounter)

def choose_path():
    print("\nMihin suuntaan haluat mennä?")
    directions = ["VASEN", "OIKEA", "ETEENPÄIN", "TAAKSEPÄIN"]
    for direction in directions:
        print(f"Komento: {direction}")
    choice = input("Suunta: ").lower().strip()
    if choice in ["vasen", "oikea", "eteenpäin", "taaksepäin"]:
        explore_place(random.choice(list(places.keys())))
    else:
        print("Virheellinen valinta. Yritä uudelleen.")
        choose_path()

def restart_game():
    print("\nOlet kuollut ja peli alkaa uudestaan...")
    main()

def main():
    print("Tervetuloa peliin!")
    role = choose_role()
    global player
    player = initialize_player(role)
    while player["health"] > 0:
        choose_path()
    restart_game()

if __name__ == "__main__":
    main()
