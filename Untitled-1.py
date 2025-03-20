def calculadora():
    try:
        n1=int(input('Digite um numero?'))
        n2=int(input('Digite outro numero?'))
        operacao=input('Escolha a operação(+,-<*,/):')
        
        if operacao=='+':
            resultado=n1+n2
        elif operacao=='-':
            resultado=n1-n2
        elif operacao=='*':
            resultado=n1*n2
        elif operacao=='/':
            resultado=n1/n2
            
        else:
            print('Operação invalida.')
            return
        print('Resultado',resultado)
        
    except ValueError:
        print('Certifique-se que é um numero.')
    except ZeroDivisionError:
        print('Erro: Divisão por zero.')
    
calculadora()