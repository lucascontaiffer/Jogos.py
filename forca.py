import random
def jogar_forca():
    print('    \'/\/\/\'/      ')
    print('     )======(       ')
    print("   .'  LOOT  '.     ")
    print('  /    _||__   \    ')
    print(' /    (_||_     \   ')
    print('|     __||_)     |  ')
    print('"       ||       "  ')
    print(' .______________.   ')
    palavras = ['banana', 'chave', 'games', 'goiabada', 'pizza']
    palavra_secreta = random.choice(palavras)

    enforcou = False
    acertou = False
    # enqunato não enforcou e não acertou
    #while(não enforcou e não acertou)
    #while(not enforcou and not acertou)
    #while(not true and not true): igual a, enquanto não for true o enforcou, e o acertou não for true, ele continuara rodando.
    while (not enforcou and not acertou):
        tentativa = input('Adicione apenás:')

        
        for letter in tentativa:
            if tentativa == palavra_secreta:
                print("Você acertou {} letras".format(tentativa))
            print(letter)

if __name__ == '__main__':
    jogar_forca()