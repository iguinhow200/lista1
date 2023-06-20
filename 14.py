pesopeixe=float(input('qual o peso do peixe ? '))
multa=round((pesopeixe-50)*4 ,2)
pesomulta=pesopeixe-50
if multa>0 :
    print(f'o valor da multa é {multa}R$ você excedeu o limite em {pesomulta}kg')

else:
    print('parabens não havera multa')

