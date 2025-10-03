num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if num2 == 0:
    print("Não é possível dividir por zero.")
elif num1 % num2 == 0:
    print("O primeiro número é divisível pelo segundo.")
else:
    print("O primeiro número NÃO é divisível pelo segundo.")
