def onKelvollinen(rivi):
    virheelliset_merkit = {'*', '#', '@'}
    for merkki in rivi:
        if merkki in virheelliset_merkit:
            return False
    return True

def main():
    try:
        with open("merkkijonoja.txt", "r") as tiedosto:
            for rivi in tiedosto:
                rivi = rivi.strip()
                if onKelvollinen(rivi):
                    print(f"{rivi} kelpaa salasanaksi.")
                else:
                    print(f"{rivi} sisältää virheellisiä merkkejä.")
    except IOError:
        print("Tiedoston avaamisessa tapahtui virhe.")

if __name__ == "__main__":
    main()
