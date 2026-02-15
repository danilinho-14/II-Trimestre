# Crie uma lista com vários elementos, gere uma lista inversa e verifique se a ordem dos elementos é igual
lista = [1, 0, 0, 0, 1]

if lista == lista[::-1]:
    print("A sua lista é um palíndromo")
else:
    print("A sua lista não é um palíndromo")
