import sys

orszag_lakossag = dict()

with open(sys.argv[1], "r") as f:
    # Az állomány eltárolása
    text = f.readlines()
    # Soronkénti olvasás
    for line in text:
        sor = line.strip().split(";")
        orszag = sor[0]
        lakossag = int(sor[2])

        # Dict feltöltése
        try:
            orszag_lakossag[orszag] += lakossag
        except KeyError:
            orszag_lakossag[orszag] = lakossag

# Dict rendezése
# lakosság szerint csökkenő sorrendbe: -kv[1]
# abc szerint növekvő sorrendbe: kv[0]
sorted_dict = sorted(orszag_lakossag.items(), key=lambda kv:(-kv[1], kv[0]))

# Minta szerinti kiíratás
for key, value in sorted_dict:
    print("{0} ({1} fő)".format(key, value))