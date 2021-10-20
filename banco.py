print('=========='*20)
print('BANCO DEV')
print('=========='*20)
valor=int(input('digite o valor que deseja sacar: R$'))
total=valor
ced=50
totced=0
while True:
    if total>=ced:
        total-=ced
        totced+=1
    else:
        if totced>0:
            print(f'total de {totced} cédulas de R$ {ced}')
        if ced==50:
            ced=20
        if ced==20:
            ced=10
        if ced==10:
            ced=1
        totced=0
        if total==0:
            break
#esse so consegui vendo o guanabara pois não tive a minima idéia de como fazer

