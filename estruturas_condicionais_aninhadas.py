conta_normal = True
conta_universitaria = True
conta_especial = False

saldo = 1000
saque = 1400
check_especial = 400

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saldo + check_especial >= saque:
        print("Saque realizado com uso do check especial!")
    else:
        print("Saldo insuficiente para realizar o saque!")
elif conta_universitaria:
        if saldo >= saque:
            print("Saque realizado com sucesso!")
        else:
            print("Saldo insuficiente para realizar o saque!")
else:
     print("Tipo de conta inválida!")
