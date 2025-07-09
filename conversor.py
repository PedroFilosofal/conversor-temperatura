def celcius_para_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_para_celcius(f):
    return (f -32) * 5/9
    
print("=== Conversor de Temperatura ===")
print("1 - Celcius para Fahrenheit")
print("2 - Fahrenheit para Celcius")

opcao = input("Escolha uma opção (1 ou 2): ")

if opcao == "1":
    c = float(input("Digite a temperatura em Celcius: "))
    f = celcius_para_fahrenheit(c)
    print(f"{c:.1}°C equivalem a {f:.1f}°F")
elif opcao == "2":
    f = float(input("Digite a temperatura em Fahrenheit: "))
    c = fahrenheit_para_celcius(f)
    print(f"{f:.1}°F equivalem a {c:.1f}°C")
else:
    print("Opção inválida.")