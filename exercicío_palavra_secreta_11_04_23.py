import os

palavra_secreta = 'Amor'
lertras_acertadas = ''
numeros_tentaivas = 0

while True:  
    letra_digitadas = input('Digite uma letra: ')
    numeros_tentaivas +=  1
    
    if len(letra_digitadas) > 1:
        print('Digite apenas uma letra')
        continue
    
    if letra_digitadas in palavra_secreta: 
        lertras_acertadas += letra_digitadas
    
    palavra_formada = ''    
    for letra_secreta in palavra_secreta:
        if letra_secreta in lertras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    
    print('Palavra formada: ', palavra_formada)    
           
    if palavra_formada == palavra_secreta:
        os.system('clear')
        print('VOCÊ GANHO !!! PARABÉNS')
        print('Palavra formada: ', palavra_secreta)           
        print('Tentativas:', numeros_tentaivas)
        lertras_acertadas = ''
        numeros_tentaivas = 0
          