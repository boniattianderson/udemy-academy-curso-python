entrada = input('Digite seu número: ')
entrada_int = int(entrada)

def par_impar(numeros):
    entrada = numeros % 2 == 0    
    if entrada:
        return f'{numeros} é par'
    return f'{numeros} é impar'

entrada = par_impar(entrada_int)
print(entrada)