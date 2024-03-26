login="abc"
senha="123"
x=1
while x<=3:
    l=input(" Digite seu login: ")
    if l==login:
        while x<=3:
            s=input(" Digite a sua senha: ")
            if s==senha:
                print(" Acesso Concedido ")
                x=4
            else:
                print(" Acesso Negado ")
                x+=1
    else:
        print(" Acesso Negado ")
        x+=1
if x==3:
    print(" Usuario Bloqueado ")
