class House:
    def __init__(self,terulet,ertek,telepules,tipus,szobakSzama ):
        self.terulet = terulet
        self.ertek = ertek
        self.telepulés = telepules
        self.tipus = tipus
        self.szobakSzama = szobakSzama 

    def __str__(self) -> str:
        return f"Eladó egy {terulet} négyzetméteres {telepules}-en található {szobakSzama} szobás {tipus} most csak {ertek} Forintért."

terulet = int(input("Írja be a lakás alapterületét (nm): "))
ertek = int(input("Írja be a lakás árát (Ft): "))
telepules =str(input("Adja meg a lakás helyszínét (település): "))
tipus = str(input("Ajda meg a lakás típusát (panellakás, kertesház, stb.): "))
szobakSzama = int(input("Adja meg a szobák számát: "))
elsohaz = House(terulet,ertek,telepules,tipus,szobakSzama)

print(elsohaz)



