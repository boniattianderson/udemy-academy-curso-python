while True:
    entrada_1 =input('Digite um número: ')
    entrada_2 =input('Digite outro número: ')
    operador =input('Digite um operador (+-*/): ')
    
    numeros_validos = None
    ent1_for_float = 0
    ent2_for_float = 0
    try:
        ent1_for_float = float(entrada_1)
        ent2_for_float = float(entrada_2)
        numeros_validos = True
    except:
        numeros_validos = None
        
    if numeros_validos is None:
        print('Um ou ambos dos números digitados não são válidos.')
        continue
    
    operadores_permitidos = '+-*/'
    
    if operador not  in operadores_permitidos:
        print('Operador selecionado incorreto.')
        continue
    
    if len(operador) > 1:
        print('Apenas um operador e permitido por vez sem exceções.')
        continue
    
    print('Realizando sua operação. Cofira a seguir o resultado da sua operção abaixo:')
    
    if operador == '+':
        print(f'{ent1_for_float}+{ent2_for_float}=', ent1_for_float + ent2_for_float)
    elif operador == '-':
        print(f'{ent1_for_float}-{ent2_for_float}=', ent1_for_float - ent2_for_float)
    elif operador == '*':
        print(f'{ent1_for_float}*{ent2_for_float}=', ent1_for_float * ent2_for_float)
    elif operador == '/':
        print(f'{ent1_for_float}/{ent2_for_float}=', ent1_for_float / ent2_for_float)
    else:
        print('NÃo era pra ter chegado até aqui.')
    
    sair = input('Quer sair? [s]im').lower.startswith('s')
    
    if sair is True:
        break