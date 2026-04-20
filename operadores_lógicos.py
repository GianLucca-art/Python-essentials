#Operadores lógicos são usados para combinar expressões booleanas. Os principais operadores lógicos são:
# and: Retorna True se ambas as expressões forem verdadeiras.
# or: Retorna True se pelo menos uma das expressões for verdadeira.
# not: Inverte o valor lógico de uma expressão (True se for False, e vice-versa).

print(True and True and True and True)  # Retorna True
print(True and False and True) # Retorna False
print(True or False)  # Retorna True
print(False or False) # Retorna False
print(not True)      # Retorna False    
print(not False)     # Retorna True




saldo = 1000
saque = 500
limite = 400
conta_especial = True


cliente = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print (cliente) 
cliente_2 = (saque <= saldo and saque >= limite) or (conta_especial and saldo >= saque)
print(cliente_2)
cliente_3 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(cliente_3)
conta_normal_com_saldo_suficiente = (saldo >= saque and saque <= limite)
conta_especial_com_saldo_suficiente = (conta_especial and saldo >= saque)
cliente_4 = conta_normal_com_saldo_suficiente or conta_especial_com_saldo_suficiente
print(cliente_4)