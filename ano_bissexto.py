 # Exercício Python 12: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
ano=int(input("ano a ser verificado: "))
ano4=round(ano/4, 0)
if ano4*4==ano:
    print(f"{ano} é um ano bissexto")
else:
    print(f"{ano} não é um ano bissexto")