
# s = "Alô mundo"
# print(s.find("mun")) # achar parte de uma string dentro de outra
# print(s.find("ok"))
#
# x = "Um dia de sol"
# print(x.rfind("d")) # Pega o última que aparece
# print(x.find("d"))
#
# a = "um tigre, dois tigres, três tigres"
# print(a.find("tigres"))
# print(a.find("tigres",7)) #inicio = 7
# print(a.find("tigre",30))
# print(a.find("tigres",0,10)) # inicio 0, final 10

# s = "um tigre, dois tigres, três tigres"
# p = 0
#
# while(p>-1):
#     p=s.find("tigre",p)
#     if p >= 0:
#         print("Posição: %d" % p)
#         p += 1

# s = "tigre"
# print("X" + s.center(10,"-") + "X")
#
# print(s.ljust(20, ".")) # adiciona caracteres ao lado, deixando a string seja na esquerda(l) ou na direita(r)
# print(s.rjust(20, "."))

# s = "um tigre, dois tigres, três tigres"
# print(s.split("e")) # faz a separação da string com o espaço


# m = "Uma linha\noutra linha\ne mais uma\n" # Quebra de Strings
# print(m.splitlines())

# s = "um tigre, dois tigres, três tigres"
# print(s.replace("tigre","gato")) # Substituir uma palavra dentro da string
# print(s.replace("tigre", "gato", 1)) # Substitui apenas no primeiro "tigre"
# print(s.replace("tigre", "gato", 2)) # Substitui o primeiro e o segundo "tigre"
# print(s.replace("tigre","")) # tirou o "tigre" da string
# print(s.replace("","-"))

# x = " Olá "
# print(x.strip()) # strip: Retira o espaço dos dois lados, lstrip: apenas da esquerda e rstrip: apenas da direita

# z = "...///Olá///..."
# print(z.lstrip("."))
# print(z.rstrip("."))
# print(z.strip("./"))

# s = "125"
# p = "alô mundo"
#
# print(s.isalnum()) # Verifica na string se é ou não um número (True ou False)
# print(p.isalnum())

# print(s.isalpha()) # Verifica se a string possui apenas letras e números
# print(p.isalpha())

# print("771".isdigit()) # O método isdigit() retorna “Verdadeiro” se todos os caracteres na string forem dígitos, caso contrário, retorna “Falso”
# print("10.4".isdigit())
# print("10+".isdigit())


# s = "ABC"
# p = "abc"
# e = "aBc"
# print(s.isupper()) # Retorna se a string inteira é maiúscula (True ou False)
# print(p.islower()) # Retorna se a string inteira é minúscula (True ou False)
# print(e.isupper())
# print(e.islower())

# Formatação de string pelo método "format"
# print("{0} {1}".format("Alô", "Mundo"))
# print("{0} x {1} R${2}".format(5,"maçã", "1.20"))
# print("{0} {1} {0}".format("-", "x"))
# print("{1} {0}".format("primeiro", "segundo"))
# print("{0:10} {1}".format("123", "456"))
# print("X{0:10}X".format("123"))
# print("X{0:10}X".format("123456789012345"))
# print("X{0:<10}X".format("123"))
# print("X{0:>10}X".format("123"))

#Centralização
# print("X{0:^10}X".format("123"))
# print("X{0:.^10}X".format("123"))
# print("X{0:.>10}X".format("123"))
# print("X{0:!>10}X".format("123"))
# print("X{0:*^10}X".format("123"))

# Máscaras com elementos da lista
# print("{0[0]} {0[1]}".format(["123", "456"]))
# print("{0[nome]} {0[telefone]}".format({"telefone": 572, "nome": "Maria"}))
# print("{0:05}".format(5))
# print("{0:*=7}".format(32))
# print("{0:*^10}".format(123))
# print("{0:*<10}".format(123))

# Separação em milhares
# print("{0:10,}".format(7532))
# print("{0:10.5f}".format(1500.31))

# Formatação de inteiros

# print("{:b}".format(5678)) # Formata para binário
# print("{:c}".format(65)) # cod 65 da tabela ASCII
# print("{:o}".format(5678)) # Formata para octal
# print("{:x}".format(5678)) # Número hexadecimal com letras minúsculos
# print("{:X}".format(5678)) # Número hexadecimal com letras maiúsculos


# print("{:n}".format(5678))
#
# import locale
# print(locale.setlocale(locale.LC_ALL,"pt_BR.utf-8"))
#
# print("{:n}".format(5678))


palavra = input("Digite a palavra secreta:").lower().strip()
for x in range(100):
    print()
digitadas = []
acertos = []
erros = 0

while True:
    senha = ""
    for letra in palavra:
        senha += letra if letra in acertos else "."
    print(senha)
    if senha == palavra:
        print("Parabéns, você ganhou!")
        print("       ___________      ")
        print("      '._==_==_=_.'     ")
        print("      .-\\:      /-.    ")
        print("     | (|:.     |) |    ")
        print("      '-|:.     |-'     ")
        print("        \\::.    /      ")
        print("         '::. .'        ")
        print("           ) (          ")
        print("         _.' '._        ")
        print("        '-------'       ")
        break
    tentativa = input("\nDigite uma letra:").lower().strip()
    if tentativa in digitadas:
        print("VocÊ ja tetou esta letra!")
        continue
    else:
        digitadas += tentativa
        if tentativa in palavra:
            acertos += tentativa
        else:
            erros += 1
            print("Você errou!")
    print("X==:==\nX   :   ")
    print("X   0   " if erros >= 1 else "X")
    linha2 = ""
    if erros == 2:
        linha2 = "   |   "
    elif erros == 3:
        linha2 = "  \|   "
    elif erros >= 4:
        linha2 = "  \|/  "
    print(f"X{linha2}")
    linha3 = ""
    if erros == 5:
        linha3 += "  /   "
    elif erros >= 6:
        linha3 += "  / \  "
    print(f"X{linha3}")
    print("X\n===========")
    if erros == 6:
        print("Puxa, você foi enforcado!")
        print("A palavra era {}".format(palavra))
        print("    _______________         ")
        print("   /               \       ")
        print("  /                 \      ")
        print("//                   \/\  ")
        print("\|   XXXX     XXXX   | /   ")
        print(" |   XXXX     XXXX   |/     ")
        print(" |   XXX       XXX   |      ")
        print(" |                   |      ")
        print(" \__      XXX      __/     ")
        print("   |\     XXX     /|       ")
        print("   | |           | |        ")
        print("   | I I I I I I I |        ")
        print("   |  I I I I I I  |        ")
        print("   \_             _/       ")
        print("     \_         _/         ")
        print("       \_______/           ")
        break