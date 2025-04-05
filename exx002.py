def dados_basicos():
    try:
        print('Olá! Seja Bem-Vindo!')
        d1=input('Digite seu nome:')
        d2=input('DIgite sua idade:')
        d3=input('Digite a sua cidade:')
        print(f'Seu nome é {d1} , você tem {d2} anos e mora em {d3}!')
        while True:
            confirmacao = input ('Está correto? (sim/não):').lower()
            if confirmacao == 'sim':
                print('Dados confirmados. Prosseguindo...')
                break
            elif confirmacao == 'não':
                print('Resposta inválida. Digite "sim" ou "não".')
    except Exception as e:
        print(f'Ocorreu um erro.{e}')
dados_basicos()