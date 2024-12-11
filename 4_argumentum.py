import sys

def apply_multiplication(multiplier:float, numbers:list) -> list:
    for i in range(0, len(numbers)):
        # Az eredeti lista értékeit felülírjuk az új, kerekített értékkel
        numbers[i] = round(float(numbers[i]) * multiplier, 3)
    return numbers

multiplication_result = apply_multiplication((float(sys.argv[1])), sys.argv[2:])

# Konvertálás szöveges listává
szamok_str = list()
for i in multiplication_result:
    szamok_str.append(str(i))

# Felsorolás pontos vesszővel elválasztva
print(";".join(szamok_str))