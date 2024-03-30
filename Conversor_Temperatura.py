import os

def temperaturas(response):
    if response > 0 and response < 3:
        c = float(input("Digite o valor de celsius: "))
        match response:
            case 1:
                result = (1.8*c)+32
                return f"{result:.2f}"
            case 2:
                result = c + 273.15
                return f"{result:.2f}"
    elif response > 2 and response < 5:
        f = float(input("Digite o valor de Fahrenheit: "))
        match response:
            case 3:
                result = (f - 32) * 5/9
                return f"{result:.2f}"
            case 4:
                result = (f - 32) * (5/9) + 273.15
                return f"{result:.2f}"
    elif response > 4 and response < 7:
        k = float(input("Digite o valor de Kelvin: "))
        match response:
            case 5:
                result = (k - 273.15)
                return f"{result:.2f}"
            case 6:
                result = (k - 273.15) * 9/5 + 32
                return f"{result:.2f}"

def dict_opcoes():
    values = ""
    for chave,valor in opcoes.items():
        values += f"{chave}) {valor}\n"
    print (values)

def limpar_terminal():
    return os.system("cls")

def valor_final(value_final):
    if response > 0 and response < 3:
        final = f"A temperatura é {value_final}°C"
        return final
    elif response > 2 and response < 5:
        final = f"A temperatura é {value_final}°F"
        return final
    else:
        final = f"A temperatura é {value_final}°K"
        return final

opcoes = {
    1 : "Celsius para Fahrenheit",
    2 : "Celsius para Kelvin",
    3 : "Fahrenheit para Celsius",
    4 : "Fahrenheit para Kelvin",
    5 : "Kelvin para Celsius",
    6 : "Kelvin para Fahrenheit",
}


while True:

    print("Seja Bem-Vindo a seu conversor de Temperaturas!🌡")
    dict_opcoes()

    while True:
            try:
                response = int(input("Escolha uma das opções acima: "))
                if response > 0 and response < 7:
                    value_final=temperaturas(response)
                    break
                else:
                    limpar_terminal()
                    dict_opcoes()
                    print("Digite um número que esteja dentro das opções !❌⚠\n")
                    continue
            except ValueError:
                limpar_terminal()
                dict_opcoes()
                print("Digite somente números inteiros❌⚠\n")
                continue

    finalizacao = valor_final(value_final)
    print(finalizacao)

    restart = input("Deseja recomeçar?").lower().startswith("s")

    if restart:
        limpar_terminal()
        continue
    else:
        print("\nAté Mais !😊")
        break