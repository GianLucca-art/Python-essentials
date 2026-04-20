saldo = 2000
saque = 5000
cheque_especial = 3000

status = "sucesso" if saldo + cheque_especial >= saque else "falha"
print (f"saque {status}!")
