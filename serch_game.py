import adivinhacao
import forca
import conversor_de_moedas
import pedra_papel_e_tesoura

def escolhe_jogo():
    print("-<*-*><*-*><*-*><*-*><*-*><*-*><*-*><*-*><*-*><*-*><*-*><*-*><*-*><*-*><*-*>-")
    print("-│&#&││&#&││&#&││&#&││&#&││&#&││&#&││&#&││&#&││&#&││&#&││&#&││&#&││&#&││&#&│-")
    print("-\$*$/\$*$/\$*$/\$*$/\$*$/\$*$/\$*$/\$*$/\$*$/\$*$/\$*$/\$*$/\$*$/\$*$/\$*$/-")
    print('Bem', 'vindos', 'ao', 'perola', 'negra', 'senhoras', 'e', 'sonhores.', sep='<*-*>')
    print("-/$^$\_ /$*$\_ /$*$\_ /$*$\_ /$*$\_ /$*$\_ /$*$\_ /$*$\_ /$*$\_ /$*$\_ /$*$\_ ")
    print("-<*-*>- <*-*>- <*-*>- <*-*>- <*-*>- <*-*>- <*-*>- <*-*>- <*-*>- <*-*>- <*-*>- ")
    print("-│&#&│--│&#&│--│&#&│--│&#&│--│&#&│--│&#&│--│&#&│--│&#&│--│&#&│--│&#&│--│&#&│-")

    print('----------------------------(-)ESCOLHA SEU JOGO(-)----------------------------')
    print('(1) Adivinhação. (2) Forca. (3) Conversor de Moedas. (4) Pedra, Papel e tesoura.')
    jogo = int(input('Escolha um jogo:'))

    if jogo == 1:
        print('Jogando adivinhação')
        adivinhacao.jogar_adivinhacao(); # Ou depois do ponto apenas jogar
    elif jogo == 2:
        print('Jogando forca')
        forca.jogar_forca();
    elif jogo == 3:
        print('Jogando conversor de moedas')
        conversor_de_moedas.jogar_conversor_de_moedas();
    elif jogo == 4:
        print('Jogando pedra,papel e tesoura')
        pedra_papel_e_tesoura.jogar_pedra_papel_tesoura();
if __name__ == '__main__':
    escolhe_jogo()