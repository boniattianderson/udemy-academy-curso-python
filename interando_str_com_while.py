frase = 'Python é uma linguagem dinamica e de tipagem forte' \
    'criada por  Guido Van Rossum'
    
i = 0 
qtd_apareceu_mais_vezes = 0
letra_que_apareceu_mais_vezes = ''
while i < len(frase):
    letra_atual = frase[i]
    
    if letra_atual == ' ':
        i += 1
        continue
    
    quantas_vezes_letra_apareceu = frase.count(letra_atual)
    
    if qtd_apareceu_mais_vezes < quantas_vezes_letra_apareceu:
        qtd_apareceu_mais_vezes = quantas_vezes_letra_apareceu
        letra_que_apareceu_mais_vezes = letra_atual
    i += 1
        
print('A letra que apreceu mais vezes foi '
      f'"{letra_que_apareceu_mais_vezes}" que apareceu '
      f'{qtd_apareceu_mais_vezes}x')