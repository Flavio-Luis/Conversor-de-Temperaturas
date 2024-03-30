import os

def temperaturas(response): # function para capturar qual conversão o usuário deseja realizar
    if response > 0 and response < 3:
        c = float(input("Digite o valor de celsius: ")) #capturando input do usuário
        match response: # utilizando math/caso para entrar no cálculo que o usuário deseja
            case 1:
                result = (1.8*c)+32
                return f"{result:.2f}"
            case 2:
                result = c + 273.15
                return f"{result:.2f}"
    elif response > 2 and response < 5: # criei outra comparação, para que ele crie uma nova variavel
        f = float(input("Digite o valor de Fahrenheit: "))
        match response:
            case 3:
                result = (f - 32) * 5/9
                return f"{result:.2f}"
            case 4:
                result = (f - 32) * (5/9) + 273.15
                return f"{result:.2f}"
    elif response > 4 and response < 7: # criei outra comparação, para que ele crie uma nova variavel
        k = float(input("Digite o valor de Kelvin: "))
        match response:
            case 5:
                result = (k - 273.15)
                return f"{result:.2f}"
            case 6:
                result = (k - 273.15) * 9/5 + 32
                return f"{result:.2f}"

def dict_opcoes(): # função para exibir o dicionário com as chaves e valores no terminal
    values = ""
    for chave,valor in opcoes.items():
        values += f"{chave}) {valor}\n"
    print (values)

def limpar_terminal(): # função para limpar o terminal windows 
    return os.system("cls")

def valor_final(value_final): # função para exibir a mensagem final
    if response > 0 and response < 3: 
        final = f"A temperatura é {value_final}°C"
        return final
    elif response > 2 and response < 5:
        final = f"A temperatura é {value_final}°F"
        return final
    else:
        final = f"A temperatura é {value_final}°K"
        return final

opcoes = { # criação do dict
    1 : "Celsius para Fahrenheit",
    2 : "Celsius para Kelvin",
    3 : "Fahrenheit para Celsius",
    4 : "Fahrenheit para Kelvin",
    5 : "Kelvin para Celsius",
    6 : "Kelvin para Fahrenheit",
}


while True: # loop que possibilita recomeçar o programa

    print("Seja Bem-Vindo a seu conversor de Temperaturas!🌡") # início do programa
    dict_opcoes()

    while True: # loop de verificação caso casa no except do try/except
            try: # validação para que o usuário não digite letras e nem números decimais
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
    print(finalizacao) # exibição do resultado na tela

    restart = input("Deseja recomeçar?").lower().startswith("s") # variavel que recebe a resposta do usuário

    if restart: # condição que verifica se recoça ou não o programa
        limpar_terminal()
        continue
    else:
        print("\nAté Mais !😊")
        break
