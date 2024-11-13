from mon_calculateur import addition, soustraction, multiplication, division

# Test des fonctions
a = 10
b = 5

print(f"Addition : {a} + {b} = {addition(a, b)}")
print(f"Soustraction : {a} - {b} = {soustraction(a, b)}")
print(f"Multiplication : {a} * {b} = {multiplication(a, b)}")
try:
    print(f"Division : {a} / {b} = {division(a, b)}")
except ValueError as e:
    print(e)