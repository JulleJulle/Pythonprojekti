import random

# Pelaajan alkutiedot
def initialize_player():
    return {
        "health": 100,
        "gold": 0,
        "inventory": {
            "sword": False,
            "shield": False,
            "armor": False,
            "boots": False,
            "food": 0,
            "potions": 0,
            "keys": 0
        },
        "experience": 0,
        "level": 1
    }

player = initialize_player()

# Vihollinen lista ja lore (lisätty helppoja vihollisia ja tehty vaikeammista vaikeampia)
enemies = {
    "rat": {"health": 5, "gold": 1, "lore": "Pieni rotta, joka etsii ruokaa.", "strength": 1},
    "snake": {"health": 8, "gold": 2, "lore": "Vaarallinen käärme, joka lymyilee ruohikossa.", "strength": 1},
    "wolf": {"health": 12, "gold": 4, "lore": "Nälkäinen susi, joka vaeltelee metsissä.", "strength": 2},
    "goblin": {"health": 15, "gold": 5, "lore": "Pieni ja viekas olento, joka rakastaa kultaa.", "strength": 2},
    "orc": {"health": 25, "gold": 10, "lore": "Suuri ja vahva hirviö, joka asuu luolissa.", "strength": 3},
    "troll": {"health": 40, "gold": 15, "lore": "Hidas mutta voimakas hirviö, joka asuu siltojen alla.", "strength": 5},
    "undead_knight": {"health": 50, "gold": 30, "lore": "Muinaisen kuninkaan kirous, joka on noussut haudastaan.", "strength": 6},
    "giant_spider": {"health": 35, "gold": 12, "lore": "Pelottava hämähäkki, joka kutoo verkkoja metsiin.", "strength": 4},
    "bandit": {"health": 20, "gold": 7, "lore": "Konna, joka ryöstää kulkijoita teiden varsilla.", "strength": 3},
    "dragon": {"health": 100, "gold": 50, "lore": "Muinaisaikojen peto, joka vartioi aarretta.", "strength": 10}
}

# Kauppa
shop_items = {
    "sword": {"price": 5, "bought": False},
    "shield": {"price": 4, "bought": False},
    "armor": {"price": 8, "bought": False},
    "boots": {"price": 3, "bought": False},
    "food": {"price": 1, "bought": 0},
    "potions": {"price": 3, "bought": 0},
    "keys": {"price": 2, "bought": 0}
}

# Dungeoneita ja lore
dungeons = {
    "Goblin Cave": {"lore": "Pimeä luola täynnä goblineja. Kuuluu kumea kähinä.", "enemies": ["goblin", "goblin", "orc"]},
    "Orc Camp": {"lore": "Vaarallinen leiri, jossa orkit harjoittelevat taistelua.", "enemies": ["orc", "orc", "troll"]},
    "Ancient Ruins": {"lore": "Muinaisten aikojen rauniot, joissa kummittelee.", "enemies": ["undead_knight", "troll", "dragon"]},
    "Bandit Hideout": {"lore": "Rosvojen piilopaikka, jossa he suunnittelevat ryöstöretkiään.", "enemies": ["bandit", "bandit", "orc"]},
    "Spider Nest": {"lore": "Hämähäkkien pesä, joka on täynnä verkkoja ja vaaroja.", "enemies": ["giant_spider", "giant_spider", "troll"]}
}

# Uusia paikkoja ja tapahtumia
places = {
    "forest": {"lore": "Tiheä metsä, jossa voi piillä vaaroja tai aarteita.", "event": "random"},
    "village": {"lore": "Rauhallinen kylä, jossa voit levätä ja käydä kaupassa.", "event": "shop"},
    "castle": {"lore": "Vanha linna, jossa huhutaan olevan aarre. Tarvitset avaimen.", "event": "dungeon"},
    "lake": {"lore": "Kaunis järvi, jonka ympärillä voi kohdata yllätyksiä.", "event": "random"},
    "mountain": {"lore": "Korkea vuori, jossa asuu vaarallisia olentoja.", "event": "dungeon"},
    "desert": {"lore": "Kuuma ja kuiva autiomaa, jossa voi kohdata vaarallisia olentoja.", "event": "random"},
    "swamp": {"lore": "Kostea ja pimeä suo, jossa piilee vaaroja.", "event": "random"}
}

def print_status():
    print(f"\nHP: {player['health']}, Kulta: {player['gold']}, Kokemus: {player['experience']}, Tasot: {player['level']}")

def level_up():
    if player["experience"] >= player["level"] * 10:
        player["level"] += 1
        player["experience"] = 0
        player["health"] = 100
        print(f"\nOnneksi olkoon! Olet noussut tasolle {player['level']} ja terveydet on palautettu!")

def fight_enemy(enemy):
    print(f"\nLöydät {enemy} ({enemies[enemy]['lore']}).")
    if enemies[enemy]["strength"] > 3 and not (player["inventory"]["sword"] and player["inventory"]["shield"] and player["inventory"]["armor"]):
        print("VAROITUS: TAPPELU TÄTÄ VIHOLLISTA VASTAAN VOI KOITUA KUOLEMAKSI ilman miekkaa, kilpeä ja haarniskaa.")
    
    choice = input("Haluatko tapella tätä vihollista vastaan? KYLLÄ/EI: ").lower().strip()
    if choice == "kyllä":
        enemy_health = enemies[enemy]["health"]
        while enemy_health > 0 and player["health"] > 0:
            print_status()
            print("\nValitse toiminto: HYÖKKÄÄ/PARANNA/PAKKENE")
            action = input("Toiminto: ").lower().strip()
            if action == "hyökkää":
                if player["inventory"]["sword"]:
                    damage = random.randint(10, 20)
                else:
                    damage = random.randint(1, 10)
                enemy_health -= damage
                print(f"Teit {damage} vahinkoa {enemy}lle.")
            elif action == "paranna" and player["inventory"]["food"] > 0:
                heal = random.randint(5, 15)
                player["health"] += heal
                player["inventory"]["food"] -= 1
                print(f"Parannat itseäsi {heal} HP:llä. Sinulla on nyt {player['health']} HP.")
            elif action == "paranna" and player["inventory"]["potions"] > 0:
                heal = random.randint(10, 25)
                player["health"] += heal
                player["inventory"]["potions"] -= 1
                print(f"Käytät parannusjuoman ja parannat itseäsi {heal} HP:llä. Sinulla on nyt {player['health']} HP.")
            elif action == "pakene":
                print(f"Pakeni {enemy}lta.")
                return
            else:
                print("Virheellinen komento tai ei riittävästi resursseja.")
            
            if enemy_health > 0:
                damage = random.randint(1, 10)
                if player["inventory"]["shield"]:
                    damage -= random.randint(1, 5)
                if damage < 0:
                    damage = 0
                player["health"] -= damage
                print(f"{enemy} teki {damage} vahinkoa sinulle.")
        
        if player["health"] > 0:
            print(f"Voitit {enemy}n ja sait {enemies[enemy]['gold']} kultaa sekä {enemies[enemy]['strength']} kokemuspisteitä!")
            player["gold"] += enemies[enemy]["gold"]
            player["experience"] += enemies[enemy]["strength"]
            level_up()
        else:
            print(f"Hävisit {enemy}lle ja kuolit...")
            restart_game()

def shop():
    while True:
        print("\nTervetuloa kauppaan! Mitä haluat ostaa?")
        for item, info in shop_items.items():
            if item == "food" or item == "potions" or item == "keys":
                print(f"{item.upper()} 1 kulta (sinulla on {player['inventory'][item]})")
            elif not info["bought"]:
                print(f"{item.upper()} {info['price']} kultaa")
        
        print("Komento POISTU KAUPASTA")
        choice = input("Mitä haluat ostaa?: ").lower().strip()
        if choice in shop_items:
            if choice in ["food", "potions", "keys"]:
                if player["gold"] >= shop_items[choice]["price"]:
                    player["gold"] -= shop_items[choice]["price"]
                    player["inventory"][choice] += 1
                    print(f"Ostit {choice}. Sinulla on nyt {player['inventory'][choice]} {choice}a.")
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
        if player["inventory"]["keys"] > 0:
            player["inventory"]["keys"] -= 1
            dungeon = random.choice(list(dungeons.keys()))
            explore_dungeon(dungeon)
        else:
            print("Tarvitset avaimen päästäksesi linnaan.")
    else:
        encounter = random.choice(list(enemies.keys()))
        fight_enemy(encounter)

def choose_path():
    print("\nMihin suuntaan haluat mennä?")
    directions = ["VASEN", "OIKEA", "ETEENPÄIN", "TAKAISEIN"]
    for direction in directions:
        print(f"Komento: {direction}")
    choice = input("Suunta: ").lower().strip()
    if choice in ["vasen", "oikea", "eteenpäin", "taaksepäin"]:
        explore_place(random.choice(list(places.keys())))
    else:
        print("Virheellinen valinta. Yritä uudelleen.")
        choose_path()

def restart_game():
    global player
    player = initialize_player()
    print("\nOlet kuollut ja peli alkaa uudestaan...")
    main()

def main():
    print("Tervetuloa peliin!")
    while player["health"] > 0:
        choose_path()
    restart_game()

if __name__ == "__main__":
    main()
zsdfxgchvjb