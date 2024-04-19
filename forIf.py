def obter_inteiro():
#definimos uma funçao
    while True:
        try:
            valido = int(input("Digite um inteiro"))
            return valido
        except ValueError:
            print("Por favor digite um numero inteiro")

numero = obter_inteiro() + 1
#recebe  numero a ser utilizado pelo laço
#de repeticao
for numero in range(numero):
#para numero dentro de numero executa
    if numero % 3 == 0 and numero != 0:
#se o numero da divisão do numero por 2 for 0 executa
        print(numero, "é divisivel por 3")
    else:
#if numero % 3 == 2:
#se o numero da divisão do numero por 2 for 1 executa
        print(numero, "não e divisivel por 3")
