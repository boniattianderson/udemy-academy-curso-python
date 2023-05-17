def multiplica(*args):
    entradas = 1 
    for numero in args:
        entradas *= numero
    return entradas

n1 = input('Digite um número: ')
n2 = input('Digite um número: ')
n1forFloat = float(n1)
n2forFloat = float(n2)
Entradas = multiplica(n1forFloat, n2forFloat)
print(f'{Entradas:,.1f}')