valorhora=float(input('digite o valor que você ganha por hora '))
qtdhoras=int(input('digite quantas horas você trabalhou este mês '))
bruto=valorhora*qtdhoras
ir=bruto*0.08
sindicato=bruto*0.05
inss=bruto*0.11
liquido=bruto-(inss+sindicato+ir)
print(f'o seu salario bruto é {bruto}R$')
print(f'você deverá pagar {inss}R$ de inss')
print(f'você devera pagar {sindicato}R$ de sindicato')
print(f'você devera pagar {ir}R$ de imposto de renda')
print(f'o seu salario liquido sera de {liquido}R$')
