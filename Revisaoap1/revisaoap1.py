disp_1=40
disp_2=40
disp_3=40
disp=disp_1+disp_2+disp_3
while disp>=0:
    quant=int(input(" Digite a quantidade de ingressos "))
    quant_estud=int(input(" Digite quantos são estudantes "))
    print(f" A sala 1 tem {disp_1} lugares disponiveis ")
    print(f" A sala 2 tem {disp_2} lugares disponiveis ")
    print(f" A sala 3 tem {disp_3} lugares disponiveis ")
    sala=int(input(" Digite qual é a sala "))
    if sala==1:
        if quant>disp_1:
            print(" Não é possível ")
        else:
            preço=30
            disp_1-=quant
    elif sala==2:
        if quant>disp_2:
            print(" Não é possível ")
        else:
            preço=30
            disp_2-=quant
    elif sala==3:
        if quant>disp_3:
            print(" Não é possível ")
            disp=-1
        else:
            preço=30
            disp_3-=quant
    total=(preço*(quant-quant_estud))+(preço/2*quant_estud)
    print(total)
    
