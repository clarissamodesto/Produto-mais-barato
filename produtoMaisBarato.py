'''
Nome: Clarissa Cruz
Data: 29/10/2024
Versão 1
'''

#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre o mais barato. 

produto1 = float (input('Digite o valor do produto 1: '))
produto2 = float (input('Digite o valor do produto 2: '))
produto3 = float (input('Digite o valor do produto 3: '))

if produto2 >= produto1 <= produto3:
    print('Você deve comprar o produto 1')
elif produto1 >= produto2 <= produto3:
    print('Você deve comprar o produto 2')
else:
    print('Você deve comprar o produto 3')