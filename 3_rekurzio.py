# rekurzió
# n-től indulunk visszafelé
# Ha n = 4 a rekurzió az aljához ér és elindul visszafelé a 4-hez kapott értékkel,
# tehát a kilépési feltételünk n = 4.

def sum(n):
    # Kilépési feltétel
    if n == 4:
        return n**2 - 2*n
    # Minden n-hez tartozó érték összege
    # (Pl.: 6-hoz, 5-höz és végül 4-hez)
    return (n**2 - 2*n) + sum(n-1)

# A bemenetekhez számított értékek eltárolása
szamok = list()
def main():
    # Első szám bekérése
    n = int(input("Adj meg egy számot: "))
    while True:
        # Beolvasás megszakítása
        if n < 0: break
        # A kiszámított összegek listához fűzése
        szamok.append(sum(n))
        # A következő szám bekérése
        n = int(input())

# main függvény meghívása
if __name__ == "__main__":
    main()

# Kiíratás
for i in szamok:
    print(i, end=" ")