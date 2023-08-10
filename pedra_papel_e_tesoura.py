import random
def jogar_pedra_papel_tesoura():
    print('HELLO WORLD!!!');

    total_de_rodadas = 6
    rodada = 1

    your_point = 0
    enemy_points = 0
    while rodada <= total_de_rodadas:
        print('rodadas {} de {}'.format(rodada, total_de_rodadas))
        you = input('you can play (1) Rock (2) Paper (3) Cisors:?')
        # Adversario
        # Pedra papel e tesoura
        possibility = ['Rock','Paper','Cisors']
        enemy = random.choice(possibility)
        print(enemy)

        if you == enemy:
            continue;

        if enemy == 'Rock' and you == 'Paper':
            print('You win!');
            your_point = your_point + 1 ;
        elif you == 'Rock' and enemy == 'Paper':
            print('You lose!')
            enemy_points = enemy_points + 1;
        elif enemy == 'Paper' and you == 'Cisors':
            print('Yow win!');
            your_point = your_point + 1;
        elif you == 'Paper' and enemy == 'Cisors':
            print('You lose!');
            enemy_points = enemy_points + 1;
        elif enemy == 'Cisors' and you == 'Rock':
            print('You win!');
            your_point = your_point + 1;
        elif you == 'Cisors' and enemy == 'Rock':
            print('You lose!');
            enemy_points = enemy_points + 1;
        rodada = rodada + 1

    print('Seus pontos:', your_point)
    print('Pontos do inimigo:', enemy_points)
    if your_point == enemy_points:
        print('Empate!')
    elif your_point > enemy_points:
        print('Você ganhou!');
    elif your_point < enemy_points:
        print('Você perdeu!')


    print('Fim')
if __name__ == '__main__':
    jogar_pedra_papel_tesoura()