MAIOR_IDADE = 18
IDADE_MINIMA = 17
idade = int(input("Digite a sua idade:"))

if idade >= MAIOR_IDADE:
    print("Você é maior de idade, pode tirar a carteira de motorista")
else: 
    print("Você é menor de idade, não pode tirar a carteira de motorista")
    
if idade < IDADE_MINIMA:    
    print("Você é muito jovem, não pode fazer a autoescola")
elif idade == IDADE_MINIMA:
    print("Você pode fazer a autoescola, mas só poderá tirar a carteira de motorista quando completar 18 anos")


