import random
def jogar_adivinhacao():
    print('(-_-$______$______$-_-)')
    print('(-_-)$HELLO WORLD$(-_-)')
    print('(-_-$______$______$-_-)')
    print('      ----||----       ')
    print('          ||           ')
    print('          ||           ')
    print('         (--)          ')
    print('       (< () >)        ')
    print('         (||)          ')
    print('         ||||          ')
    print('         ||||          ')
    print('         ||||          ')
    print('         \||/          ')
    print('          \/           ')

    secret_key = random.randrange(1, 101);

    total_de_tentativas = 0
    rodada = 1
    pontos = 1000

    print('Qual nível de dificuldade você quer?')
    print('(1) Fácil (2) Médio (3) Difícil')

    nivel = int(input('Defina o nível:'))

    if nivel == 1:
        total_de_tentativas = total_de_tentativas + 20;
    elif nivel == 2:
        total_de_tentativas = total_de_tentativas + 10;
    elif nivel == 3:
        total_de_tentativas = total_de_tentativas + 5;

    while rodada <= total_de_tentativas:
        print('tentativa {} de {}'.format(rodada, total_de_tentativas));
        tentativa = int(input('Tente acertar o número:?'));
        print('O número digitado foi: ',tentativa);

        if tentativa < 1 or tentativa > 100:
            print('Digite um número entre 1 e 100');
            continue;

        if tentativa == secret_key:
            print('Você acertou, parabéns com {} ponto!!!'.format(pontos));
            break;
        else:
            if tentativa < secret_key:
                print('você chutou baixo!');
            elif tentativa > secret_key:
                print('Você chutou alto!')
            pontos_perdidos = abs(secret_key - tentativa);
            pontos = pontos - pontos_perdidos;
            # Facilita muito print('Você perdeu', pontos_perdidos)
            # Facilita muito print(pontos)
        rodada = rodada +1

    print('!!!Fim!!!');
if __name__ == '__main__': # serve para executarmos nosso jogo se true dentro da pasta e dentro do terminal de jogos ele só ira abrir se selecionado
    jogar_adivinhacao()