def jogar_conversor_de_moedas():
    print('(-_-$______$______$-_-)')
    print('(-_-)$HELLO WORLD$(-_-)')
    print('(-_-$______$______$-_-)')
    print('      ----||----       ')
    print('          ||           ')
    print('         (--)          ')
    print('       (< () >)        ')
    print('         (||)          ')
    print('         ||||          ')
    print('         ||||          ')
    print('         ||||          ')
    print('         \||/          ')
    print('          \/           ')

    #Real
    dolar_to_real = 4.73;
    euro_to_real = 5.21;
    ien_to_real = 0.034;

    #Dólar
    real_to_dolar = 0.21;
    euro_to_dolar = 1.1;
    ien_to_dolar = 0.0071;

    #Euro
    real_to_euro = 0.19;
    dolar_to_euro = 0.91;
    ien_to_euro = 0.0064;


    #Ien
    real_to_ien = 29.85;
    Dolar_to_ien = 141.16;
    euro_to_ien = 155.57;
    print('  $-----$Real$-----$')
    print('     $Dólar$', dolar_to_real)
    print('     $Euro$', euro_to_real)
    print('     $Ien$', ien_to_real)

    print('Real-Dólar-Euro-Ien')
    previous = input('qual moeda deseja trocar?:')

    if previous == 'Real':
        print('Dólar-Euro-Ien')
        current_real = input('Qual moeda deseja converter para real?:')

        if current_real == 'Dólar':
            print('Dólar para real cotação', dolar_to_real);

            valor_coversao_dolar_to_real = int(input('quantos dólares deseja trocar?:'));
            print('voce vai converter {} dólares para reais'.format(valor_coversao_dolar_to_real));

            result_dolar_to_real = dolar_to_real * valor_coversao_dolar_to_real;
            print(result_dolar_to_real);
        elif current_real == 'Euro':
            print('Euro para real cotação', euro_to_real);

            valor_coversao_euro_to_brl = int(input('quantos euros deseja trocar?:'));
            print('Você vai converter {} euros para reais'.format(valor_coversao_euro_to_brl));

            result_euro_to_brl = euro_to_real * valor_coversao_euro_to_brl;
            print(result_euro_to_brl);
        elif current_real == 'Ien':
            print('Ien para real cotação', ien_to_real);

            valor_conversao_ien_to_brl = int(input('quantos iens deseja trocar?:'));
            print('Você vai converter {} Iens para reais'.format(valor_conversao_ien_to_brl));

            result_ien_to_brl = ien_to_real * valor_conversao_ien_to_brl;
            print(result_ien_to_brl);
    elif previous == 'Dólar':
        print('Real-Euro-Ien')
        current_dolar = input('qual moeda deseja converter para dolar?:')

        if current_dolar == 'Real':
            print('Dólar para real cotação', real_to_dolar);

            valor_conversao_real_to_dolar = int(input('quantos reais deseja trocar?:'));
            print('Você vai converter {} real para Dólares'.format(valor_conversao_real_to_dolar));

            result_real_to_brl = real_to_dolar * valor_conversao_real_to_dolar;
            print(result_real_to_brl);
        elif current_dolar == 'Euro':
            print('Euro para Dólar cotação',euro_to_dolar);

            valor_conversao_euro_to_dolar = int(input('quantos Euros deseja trocar?:'));
            print('Você vai converter {} euros para Dólares'.format(valor_conversao_euro_to_dolar));

            result_euro_to_dolar = euro_to_dolar * valor_conversao_euro_to_dolar;
            print(result_euro_to_dolar)
        elif current_dolar == 'Ien':
            print('Ien para Dólar cotação', ien_to_dolar);

            valor_conversao_ien_to_dolar = int(input('Quantos Iens deseja trocar?:'));
            print('Você vai converter {} iens para Dólares'.format(valor_conversao_ien_to_dolar));

            result_ien_to_dolar = ien_to_dolar * valor_conversao_ien_to_dolar;
            print(result_ien_to_dolar)
    elif previous == 'Euro':
        print('Real-Dólar-Ien');
        current_euro = input('Qual moeda deseja converter para Euro?:');

        if current_euro == 'Real':
            print('Real para Euro cotação', real_to_euro)

            valor_conversao_real_to_euro = int(input('Quantos reais deseja trocar?:'));
            print('Você vai converter {} real para Euro'.format(valor_conversao_real_to_euro));

            result_real_to_euro = real_to_euro * valor_conversao_real_to_euro;
            print(result_real_to_euro)
        elif current_euro == 'Dólar':
            print('Dólar para Euro cotação', dolar_to_euro)

            valor_conversao_dolar_to_euro = int(input('Quantos reais deseja trocar?:'));
            print('Você vai converter {} Dólar para Euro'.format(valor_conversao_dolar_to_euro));

            result_dolar_to_euro = dolar_to_euro * valor_conversao_dolar_to_euro;
            print(result_dolar_to_euro);
        elif current_euro == 'Ien':
            print('Ien para Euro cotação', ien_to_euro)

            valor_conversao_ien_to_euro = int(input('Quantos Iens deseja trocar?:'));
            print('Você vai converter {} Ien para Euro'.format(valor_conversao_ien_to_euro));

            result_ien_to_euro = ien_to_euro * valor_conversao_ien_to_euro;
            print(result_ien_to_euro);
    elif previous == 'Ien':
        print('Real-Dólar-Euro');
        current_ien = input('Qual moeda deseja converter para Ien?:');

        if current_ien == 'Real':
            print('Real para Ien cotação', real_to_ien)

            valor_conversao_real_to_ien = int(input('Quantos Iens deseja trocar?:'));
            print('Você vai converter {} Ien para Euro'.format(valor_conversao_real_to_ien));

            result_real_to_ien = real_to_ien * valor_conversao_real_to_ien;
            print(result_real_to_ien);
        elif current_ien == 'Dólar':
            print('Ien para Euro cotação', Dolar_to_ien)

            valor_conversao_Dolar_to_ien = int(input('Quantos Iens deseja trocar?:'));
            print('Você vai converter {} Ien para Euro'.format(valor_conversao_Dolar_to_ien));

            result_Dolar_to_ien = Dolar_to_ien * valor_conversao_Dolar_to_ien;
            print(result_Dolar_to_ien);
        elif current_ien == 'Euro':
            print('Ien para Euro cotação', euro_to_ien)

            valor_conversao_euro_to_ien = int(input('Quantos Iens trocar?:'));
            print('Você vai converter {} Ien para Euro'.format(valor_conversao_euro_to_ien));

            result_euro_to_ien = euro_to_ien * valor_conversao_euro_to_ien;
            print(result_euro_to_ien);

    print('!!!LUCKYYY!!!')
if __name__ == '__main__':
    jogar_conversor_de_moedas()