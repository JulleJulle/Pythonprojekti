def laskeTEL(palkka):
    tel_maksu = palkka * 0.057
    return tel_maksu

def laskeTVM(palkka):
    tvm_maksu = palkka * 0.0065
    return tvm_maksu

def laskeVerot(palkka, veroprosentti):
    verot = palkka * (veroprosentti / 100)
    return verot

def tulostaErittely(palkka, veroprosentti):
    tel_maksu = laskeTEL(palkka)
    tvm_maksu = laskeTVM(palkka)
    verot = laskeVerot(palkka, veroprosentti)
    
    nettotulo = palkka - tel_maksu - tvm_maksu - verot
    
    print("\n" + "*" * 77)
    print("Erittely palkkaan kohdistuvista vähennyksistä antamiesi tietojen perusteella:")
    print("*" * 77)
    print(f"Ennakonpidätys: {verot:.2f}")
    print(f"- Työeläkemaksu: {tel_maksu:.2f}")
    print(f"- Työttömyysvakuutusmaksu: {tvm_maksu:.2f}")
    print("-" * 31)
    print(f"= Nettopalkka: {nettotulo:.2f}")

def main():
    palkka = float(input("Anna kuukausipalkka: "))
    veroprosentti = float(input("Anna veroprosentti: "))
    
    tulostaErittely(palkka, veroprosentti)


    input("Paina Enter lopettaaksesi...")

if __name__ == "__main__":
    main()
