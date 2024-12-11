hobbi_db = dict()

while True:
    be = input()
    if be == "": break

    be = be.split(':')
    hobbik = be[1].split(',')

    for hobbi in hobbik:
        if hobbi not in hobbi_db:
            hobbi_db[hobbi] = 1
        else:
            hobbi_db[hobbi] += 1

for key, value in sorted(hobbi_db.items()):
    print("{0}: {1} fő".format(key, value))