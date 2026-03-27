## Máquina de Vendas

**Este projeto foi evoluído após posteriormente**

Primeiro algoritmo desenvolvido durante a faculdade utilizando programação funcional.
Este projeto é uma simulação simples de uma máquina de vendas (vending machine) desenvolvida em Python.
O sistema permite que o usuário escolha produtos, insira dinheiro e receba o troco automaticamente.

### Funcionalidades

- Exibição de produtos disponíveis com preços e estoque
- Seleção de itens pelo usuário
- Entrada de dinheiro até atingir o valor do produto
- Cálculo automático do troco
- Devolução do troco em notas e moedas
- Atualização dinâmica do estoque
- Interface via terminal (CLI)

### Produtos disponíveis

- Mouse — R$30,00
- Teclado — R$40,00
- Monitor — R$500,00
- Mousepad — R$25,00
- Notebook — R$3000,00

### Como funciona

O sistema é dividido em três partes principais:

1. Seleção de produto

   O usuário escolhe um item através de um menu interativo.

2. Pagamento

   A função recebe valores digitados pelo usuário até atingir o preço do produto.

3. Troco

   O sistema calcula e devolve o troco utilizando uma lista de valores (notas e moedas).

### Estrutura do código

- maquina() → Controla o fluxo principal e o menu
- get_dinheiro() → Recebe o pagamento do usuário
- push_troco() → Calcula e exibe o troco

### Como executar

Certifique-se de ter o Python instalado
Clone o repositório:

- git clone https://github.com/JothanRAlmeida/ModeloDados_Vendas.git

Acesse a pasta do projeto:

- cd ModeloDados_Vendas

Execute o script:

- python maquina.py

### Observações

- O sistema não aceita valores inválidos (ex: texto no lugar de números)
- O estoque é atualizado apenas durante a execução (não é persistente)
- Existe uma pequena correção no cálculo de troco (+ 0.00006) para evitar problemas com ponto flutuante

### Possíveis melhorias

- Persistência de estoque (banco de dados ou arquivo)
- Interface gráfica (Tkinter ou Web)
- Melhor tratamento de erros (inputs inválidos)
- Refatoração para orientação a objetos
- Melhor algoritmo para cálculo de troco
