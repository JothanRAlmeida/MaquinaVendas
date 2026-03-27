# Preços dos produtos em reais
preco_mouse = 30.0
preco_teclado = 40.0
preco_monitor = 500.0
preco_mousepad = 25.0
preco_notebook = 3000.0

# Estoque de produtos
mouse = 5
teclado = 5
monitor = 2
mousepad = 10
notebook = 1

#Dinheiro possível para dar o troco
valores_dinheiro = [200, 100, 50, 20, 10, 5, 1, 0.5, 0.25, 0.10, 0.5, 0.1]

#Devolve o troco ao cliente
def push_troco(troco, produto):
    moeda = 0
    while troco > 0 and moeda < len(valores_dinheiro):
        if troco > valores_dinheiro[moeda]: 
            print(f"R${valores_dinheiro[moeda]}")
            troco -= valores_dinheiro[moeda]
        else:
            moeda += 1
    print(f"\nObrigado e volte sempre! Pegue o seu novo {produto}!\n")

#Recebe o dinheiro do cliente e calcula o troco
def get_dinheiro(preco):
    dinheiro = 0
    while dinheiro < preco:
        dinheiro += float(input("Insira o dinheiro: R$"))

    print(f"\nValor do produto R${preco}")
    print(f"Troco: R${dinheiro - preco}")
    print("Aqui está seu troco:")
    return dinheiro - preco + 0.00006
    
#Máquina principal para escolha do produto
def maquina(mouse, teclado, monitor, mousepad, notebook):
    while True:
        # Menu
        print("-"*25)
        print(f"PRODUTOS DISPONÍVEIS\n 1 - {mouse} Mouses - R${preco_mouse}\n 2 - {teclado} Teclados - R${preco_teclado}\n 3 - {monitor} Monitores - R${preco_monitor}\n 4 - {mousepad} Mousepads - R${preco_mousepad}\n 5 - {notebook} Notebooks - R${preco_notebook}\n 6 - Sair")
        print("-"*25)

        print("\nEscolha pelo número!")
        item = int(input("O que deseja? "))

        if item == 1 and mouse > 0:
            push_troco(get_dinheiro(preco_mouse),"mouse")
            return maquina(mouse-1,teclado,monitor,mousepad,notebook)
        elif item == 2 and teclado > 0:
            push_troco(get_dinheiro(preco_teclado),"teclado")
            return maquina(mouse,teclado-1,monitor,mousepad,notebook)
        elif item == 3 and monitor > 0:
            push_troco(get_dinheiro(preco_monitor),"monitor")
            return maquina(mouse,teclado,monitor-1,mousepad,notebook)
        elif item == 4 and mousepad > 0:
            push_troco(get_dinheiro(preco_mousepad),"mousepad")
            return maquina(mouse,teclado,monitor,mousepad-1,notebook)
        elif item == 5 and notebook > 0:
            push_troco(get_dinheiro(preco_notebook), "notebook")
            return maquina(mouse,teclado,monitor,mousepad,notebook-1)
        elif item == 6:
            break
        else:
            print("\nEscolha inválida!\n")
maquina(mouse, teclado, monitor, mousepad, notebook)