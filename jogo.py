import os
import platform
import time

os.system("cls")
os.system("title Advinhe o Jogo")
node = platform.node()

# Dicionário com os códigos ANSI para cores
color = {
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "magenta": "\033[35m",
    "cian": "\033[36m",
    "reset": "\033[0m"  # Para resetar a cor
}

print(f"Olá, {color['blue']}{node}{color['reset']}!")
time.sleep(2.0)
print(f"{color['reset']}Vou te propor um {color['red']}jogo{color['reset']}!")
time.sleep(1.5)

for i in range(1, 4):
    print("Mas primeiro" + "." * i, end="\r", flush=True)
    time.sleep(0.7)
time.sleep(1)
print("Mas primeiro...")

print(f"O seu nome é realmente {color['blue']}{node}{color['reset']}?")
resp = input("R: ")
if "Sim" in resp or "sim" in resp or "s" in resp or "ss" in resp:
    print("Ok.")
else:
    print(f"Beleza, digite seu{color['blue']} nome{color['reset']} abaixo")
    node = input(f"R: ")
    print(f"Confirmado! Agora seu nome é {color['blue']}{node}{color['reset']}.")
time.sleep(3)
os.system("cls")
print(f"Vou lhe apresentar o {color['red']}jogo{color['reset']}.")
time.sleep(1)
input(f"Pressione ENTER para avançar cada frase")
os.system("cls")
input(f"O nome dele é {color['magenta']}Advinhe o Jogo{color['reset']}!")
input(f"Para advinhar {color['cian']}o jogo{color['reset']} você deve analizar {color['yellow']}reviews{color['reset']} do {color['blue']}Steam.{color['reset']}")
input(f"Você pode {color['green']}pedir dicas {color['reset']}a qualquer momento, mas {color['red']}perderá 1 ponto {color['reset']}ao pegar uma dica")
input(f"Haverá 3 dificuldades, {color['green']}fácil{color['reset']},{color['yellow']} médio {color['reset']}e{color['red']} difícil{color['reset']}")
input(f"{color['green']}Fácil{color['reset']} = 1 ponto |{color['yellow']} Médio{color['reset']} = 2 pontos |{color['red']} Difícil {color['reset']}= 3 pontos")
input(f"A cor do nível indica a {color['red']}difículdade{color['reset']}")
input(f"Você tem {color['green']}3 reviews{color['reset']} para analizar de cada jogo")
input(f"E deve digitar {color['red']}exatamente {color['reset']}o {color['cian']}nome do jogo{color['reset']}, do jeito que exibe no{color['blue']} Steam{color['reset']}")
input(f"Você começa com {color['blue']}10 pontos{color['reset']}.")
input(f"Então vamos começar {node}!")
pontos = 10
acertou = 0

# Jogo 1

while acertou == 0:
    os.system("cls")
    print(f"{color['green']}JOGO 1{color['reset']}")
    print(f"Você possui {color['green']}{pontos} pontos{color['reset']}.")
    print("")
    print("Você consegue interagir com o jogo na caixa de resposta.")
    print("---------------------------------------------------------")
    print("Digite um número de 1 a 3 para abrir a review")
    print("Digite 'dica' para mostrar uma dica")
    print("Digite 'desistir' para pular")
    print("---------------------------------------------------------")
    print("")
    jogo = input("R: ")
    print("")
    if jogo == "1":
        os.system("cd reviews/jogo1 && 1.png")
    elif jogo == "2":
        os.system("cd reviews/jogo1 && 2.png")
    elif jogo == "3":
        os.system("cd reviews/jogo1 && 3.png")
    elif jogo == "A Way Out":
        acertou = 1
        pontos = pontos + 1
        os.system("cd reviews/jogo1 && jogo.png")
        input("Você acertou!")
    elif jogo == "dica" or jogo == "Dica":
        if pontos >= 1:
            pontos = pontos - 1
            input("Jogo coop produzido pela EA e Hazelight Studios. Essa é a formatação do jogo * *** ***")
        else:
            input("Você não tem pontos para adquirir uma dica")
    elif jogo == "desistir" or jogo == "Desistir":
        os.system("cd reviews/jogo1 && jogo.png")
        input(f"O jogo era {color['blue']}A Way Out{color['reset']}.")
        acertou = 1
    else:
        input("Resposta inválida!")

# Jogo 2

acertou = 0
while acertou == 0:
    os.system("cls")
    print(f"{color['red']}JOGO 2{color['reset']}")
    print(f"Você possui {color['green']}{pontos} pontos{color['reset']}.")
    print("")
    print("Você consegue interagir com o jogo na caixa de resposta.")
    print("---------------------------------------------------------")
    print("Digite um número de 1 a 3 para abrir a review")
    print("Digite 'dica' para mostrar uma dica")
    print("Digite 'desistir' para pular")
    print("---------------------------------------------------------")
    print("")
    jogo = input("R:")
    print("")
    if jogo == "1":
        os.system("cd reviews/jogo2 && 1.png")
    elif jogo == "2":
        os.system("cd reviews/jogo2 && 2.png")
    elif jogo == "3":
        os.system("cd reviews/jogo2 && 3.png")
    elif jogo == "Buckshot Roulette":
        acertou = 1
        pontos = pontos + 3
        os.system("cd reviews/jogo2 && jogo.png")
        input("Você acertou!")
    elif jogo == "dica" or jogo == "Dica":
        if pontos >= 1:
            pontos = pontos - 1
            input("Jogo indie de roleta russa feito por uma pessoa.")
        else:
            input("Você não tem pontos para adquirir uma dica")
    elif jogo == "desistir" or jogo == "Desistir":
        os.system("cd reviews/jogo2 && jogo.png")
        input(f"O jogo era {color['blue']}Buckshot Roulette{color['reset']}.")
        acertou = 1
    else:
        input("Resposta inválida!")

# Jogo 3

acertou = 0
while acertou == 0:
    os.system("cls")
    print(f"{color['yellow']}JOGO 3{color['reset']}")
    print(f"Você possui {color['green']}{pontos} pontos{color['reset']}.")
    print("")
    print("Você consegue interagir com o jogo na caixa de resposta.")
    print("---------------------------------------------------------")
    print("Digite um número de 1 a 3 para abrir a review")
    print("Digite 'dica' para mostrar uma dica")
    print("Digite 'desistir' para pular")
    print("---------------------------------------------------------")
    print("")
    jogo = input("R: ")
    print("")
    if jogo == "1":
        os.system("cd reviews/jogo3 && 1.png")
    elif jogo == "2":
        os.system("cd reviews/jogo3 && 2.png")
    elif jogo == "3":
        os.system("cd reviews/jogo3 && 3.png")
    elif jogo == "KinitoPET":
        acertou = 1
        pontos = pontos + 2
        os.system("cd reviews/jogo3 && jogo.png")
        input("Você acertou!")
    elif jogo == "dica" or jogo == "Dica":
        if pontos >= 1:
            pontos = pontos - 1
            input("É um jogo de terror psicológico que quebra a quarta parede.")
        else:
            input("Você não tem pontos para adquirir uma dica")
    elif jogo == "desistir" or jogo == "Desistir":
        os.system("cd reviews/jogo3 && jogo.png")
        input(f"O jogo era {color['blue']}KinitoPET{color['reset']}.")
        acertou = 1
    else:
        input("Resposta inválida!")

# Jogo 4

acertou = 0
while acertou == 0:
    os.system("cls")
    print(f"{color['green']}JOGO 4{color['reset']}")
    print(f"Você possui {color['green']}{pontos} pontos{color['reset']}.")
    print("")
    print("Você consegue interagir com o jogo na caixa de resposta.")
    print("---------------------------------------------------------")
    print("Digite um número de 1 a 3 para abrir a review")
    print("Digite 'dica' para mostrar uma dica")
    print("Digite 'desistir' para pular")
    print("---------------------------------------------------------")
    print("")
    jogo = input("R: ")
    print("")
    if jogo == "1":
        os.system("cd reviews/jogo4 && 1.png")
    elif jogo == "2":
        os.system("cd reviews/jogo4 && 2.png")
    elif jogo == "3":
        os.system("cd reviews/jogo4 && 3.png")
    elif jogo == "Ultimate Chicken Horse":
        acertou = 1
        pontos = pontos + 1
        os.system("cd reviews/jogo4 && jogo.png")
        input("Você acertou!")
    elif jogo == "dica" or jogo == "Dica":
        if pontos >= 1:
            pontos = pontos - 1
            input("É um jogo competitivo onde você cria o caminho para finalizar a fase")
        else:
            input("Você não tem pontos para adquirir uma dica")
    elif jogo == "desistir" or jogo == "Desistir":
        os.system("cd reviews/jogo4 && jogo.png")
        input(f"O jogo era {color['blue']}Ultimate Chicken Horse{color['reset']}.")
        acertou = 1
    else:
        input("Resposta inválida!")

# Jogo 5

acertou = 0
while acertou == 0:
    os.system("cls")
    print(f"{color['yellow']}JOGO 1{color['reset']}")
    print(f"Você possui {color['green']}{pontos} pontos{color['reset']}.")
    print("")
    print("Você consegue interagir com o jogo na caixa de resposta.")
    print("---------------------------------------------------------")
    print("Digite um número de 1 a 3 para abrir a review")
    print("Digite 'dica' para mostrar uma dica")
    print("Digite 'desistir' para pular")
    print("---------------------------------------------------------")
    print("")
    jogo = input("R: ")
    print("")
    if jogo == "1":
        os.system("cd reviews/jogo5 && 1.png")
    elif jogo == "2":
        os.system("cd reviews/jogo5 && 2.png")
    elif jogo == "3":
        os.system("cd reviews/jogo5 && 3.png")
    elif jogo == "Detroit: Become Human":
        acertou = 1
        pontos = pontos + 1
        os.system("cd reviews/jogo5 && jogo.png")
        input("Você acertou!")
    elif jogo == "dica" or jogo == "Dica":
        if pontos >= 1:
            pontos = pontos - 1
            input("Jogo de Androides que você faz sua própria história")
        else:
            input("Você não tem pontos para adquirir uma dica")
    elif jogo == "desistir" or jogo == "Desistir":
        os.system("cd reviews/jogo5 && jogo.png")
        input(f"O jogo era {color['blue']}Detroit: Become Human{color['reset']}.")
        acertou = 1
    else:
        input("Resposta inválida!")

print(f"{color['reset']}")