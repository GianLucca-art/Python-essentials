texto = input("Digite um texto:")

VOGAIS = "AEIOU"
CONSOANTES = "BCDFGHJKLMNPQRSTVWXYZ"


# Exemplo utilizando um iteravel (string) e um laço de repetição (for)
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end=" ")
else:
    print()
    
for letra in texto:
    if letra.upper() in CONSOANTES:
        print(letra, end=" ")
else:
    print()
    print("Fim do programa!")

#Exemplo utilizando a função built-in range() e um laço de repetição (for)
for numero in range(0, 50, 5):
    print(numero, end=" ")


    
