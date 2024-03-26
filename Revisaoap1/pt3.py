fim=1
p=10
apagar=0
while fim==1:
    cod=int(input(" Digite o código do produto ou 0 para finalizar a compra "))
    preço=0
    if cod==0:
        fim=0
        p=10
    elif cod==1:
        p=0.5
    elif cod==2:
        p=1.0
    elif cod==3:
        p=1.5
    elif cod==4:
        p=120
    else:
        print(" Código Invalido ")
    if p!=10:
        qtd=int(input(" Digite a quantidade desejada "))
        apagar=apagar+(p*qtd)
print(f" O total a pagar é de R${apagar}")

