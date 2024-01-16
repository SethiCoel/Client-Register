import os
from time import sleep


class Registro:
    clientes = []
    valor_total = []
    total_dinheiro = []
    valor_retirado = []
    notas = []

    def __init__(self, cliente, forma_pagamento, mensalidade, notas):
        self._cliente = cliente
        self._forma_pagamento = forma_pagamento
        self._mensalidade = mensalidade
        self._notas = notas
        Registro.clientes.append(self)
        Registro.valor_total.append(self._mensalidade)

    def __str__(self):
        return f'{self._cliente} {self._forma_pagamento} {self._mensalidade} {self._notas}'

    def limpar_tela():
        os.system('cls')

    @classmethod
    def listar_clientes(cls):
        Registro.sub_titulo('Lista de clientes')
        cabecalho = (f'{"Nome do cliente":<50} {"Forma de pagamento":<25} {"Mensalidade":<20} {"Notas"}')
        print(cabecalho)
        print('-' * 135)
        if not cls.clientes:
            print(f'{"-":<50} {"-":^18} {" " * 6} {"-":<20} {"-"}')
        
        else:
            for cliente in cls.clientes:
                print(f'{cliente._cliente:<50} {cliente.forma_pagamento:^18} {" " * 6} {cliente._mensalidade:<20.2f} {cliente._notas}'.replace('.',','))
            
    @property
    def forma_pagamento(self):
        if self._forma_pagamento == 1:
            return 'Dinheiro'
        
        elif self._forma_pagamento == 2:
            return 'Pix'
        
        elif self._forma_pagamento == 3:
            return 'Depósito'
    


    def sub_titulo(titulo):
        Registro.limpar_tela()
        n = len(titulo) + 6
        Registro.cor('=' * n, 'ciano')
        Registro.cor(f'{titulo.center(n)}', 'ciano')
        Registro.cor('=' * n, 'ciano')
        print()

    @classmethod
    def validar_registro(cls):
        Registro.sub_titulo('Registrar novo cliente')
        while True:
            nome_do_cliente = str(input('Digite o nome do cliente: ')).title()
            f_nome_do_cliente = ' '.join(nome_do_cliente.split())

            if f_nome_do_cliente == '':
                Registro.limpar_tela()
                Registro.sub_titulo('Registrar novo cliente')
                Registro.cor('Entrada inválida. O espaço não pode ficar em branco\n', 'vermelho')
                continue
            
            while True:
                try:
                    forma_de_pagamento = int(input('''\nForma de pagamento                                   
(1) Dinheiro
(2) Pix
(3) Depósito 

Escolha uma das opções acima. De 1 a 3: '''))
                    
                    if 1 < forma_de_pagamento > 3:
                        Registro.limpar_tela()
                        Registro.sub_titulo('Registrar novo cliente')
                        Registro.cor('Entrada inválida. Digite uma opção de 1 a 3', 'vermelho')
                        continue
            
                except ValueError:
                    Registro.limpar_tela()
                    Registro.sub_titulo('Registrar novo cliente')
                    Registro.cor('Entrada inválida. Digite apenas números', 'vermelho')
                    continue
                break

            while True:   
                try:
                    mensalidade = float(input('\nValor da mensalidade: R$').replace(',','.'))
                    break

                except ValueError:
                    Registro.limpar_tela()
                    Registro.sub_titulo('Registrar novo cliente')
                    Registro.cor('Entrada inválida. Digite apenas numeros', 'vermelho')
                    continue

            if forma_de_pagamento == 1:
                    cls.total_dinheiro.append(mensalidade)

            notas = str(input('\nAdicione uma nota a este pagamento: ')).capitalize()
            f_notas = ' '.join(notas.split())

            cliente = Registro(f_nome_do_cliente, forma_de_pagamento, mensalidade, f_notas)

            Registro.limpar_tela()
            Registro.sub_titulo('Registrar novo cliente')
            Registro.cor('Cliente registrado com sucesso!', 'verde')
            break
    
    def validar_opcao_escolhida():
        while True:
            try:
                opcao_escolhida = int(input('Escolha uma das opções acima. De 1 a 5: '))
                
                if 1 < opcao_escolhida > 5:
                    Registro.limpar_tela()
                    Registro.cor('Entrada inválida. Digite uma opção de 1 a 5', 'vermelho')
                    sleep(1)
                    return opcao_escolhida
                return  opcao_escolhida


            except ValueError as error:
                Registro.limpar_tela()
                Registro.cor('\nEntrada inválida. Digite apenas números', 'vermelho')
                sleep(1)
                
                return 6
        
    def encerrar_programa():
        Registro.limpar_tela()
        print('Encerrando Programa.')
        sleep(0.4)
        Registro.limpar_tela()

        print('Encerrando Programa..')
        sleep(0.4)
        Registro.limpar_tela()

        print('Encerrando Programa...')
        sleep(0.4)
        Registro.limpar_tela()

        Registro.limpar_tela()
        print('Encerrando Programa.')
        sleep(0.4)
        Registro.limpar_tela()

        print('Encerrando Programa..')
        sleep(0.4)
        Registro.limpar_tela()

        print('Encerrando Programa...')
        sleep(0.4)
        Registro.limpar_tela()
        Registro.cor('Programa Fechado.', 'verde')
        exit()
    
    def cor(texto, cor=''):
        if cor == 'vermelho':
            cor = '\033[0;31;40m'
       
        if cor == 'verde':
            cor = '\033[0;32;40m'

        if cor == 'amarelo':
            cor = '\033[0;33;40m'
       
        if cor == 'azul':
            cor = '\033[0;34;40m'


        if cor == 'ciano':
            cor = '\033[0;36;40m'
         

        print(f'{cor}{texto}\033[m')

    @classmethod
    def fechar_caixa(cls):
        Registro.sub_titulo('Fechar Caixa')
        soma = 0
        dinheiro = 'Total Dinheiro: -' 
        pix = 'Total Pix: -'
        deposito = 'Total Depósito: -'
       
        if not cls.valor_retirado:
            total_retirado = 'Total Retirado: -'
        else:
            for valor in cls.valor_retirado:
                soma += valor
                total_retirado = f'Total Retirado: R$-{soma:.2f}'.replace('.',',')

        

        for pagamentos in cls.clientes:
            
            if pagamentos.forma_pagamento == 'Dinheiro':
                valor_disponivel = 0
                for valor in cls.total_dinheiro:
                    valor_disponivel += valor
                dinheiro = (f'Total Dinheiro: {valor_disponivel:.2f}'.replace('.',','))
                

            elif pagamentos.forma_pagamento == 'Pix':
                pix = (f'Total Pix: {pagamentos._mensalidade:.2f}'.replace('.',','))    
            
            elif pagamentos.forma_pagamento == 'Depósito':
                deposito = (f'Total depósito: {pagamentos._mensalidade:.2f}'.replace('.',','))
            
        if not cls.valor_total:
            valor_total = 'Valor Total: -'

        else:    
            soma_total = 0
            for valor in cls.valor_total:
                soma_total += valor
                valor_total = (f'Valor Total: {soma_total:.2f}'.replace('.',','))


        print(dinheiro)
        print(pix)
        print(deposito)
        Registro.cor(total_retirado, 'vermelho')
        print()
        Registro.cor(valor_total, 'verde')

        print('\n')

        print(f'{"Saída":<10}   {"Notas":<50}')
        print('-' * 100)
        
        for valor in cls.notas:
            f_valor = f'{valor["Valor"]:.2f}'.replace('.',',')
            print(f'\033[0;31;40mR${f_valor:<10}\033[m {valor["Nota"]:<50}')





    @classmethod
    def retirar_dinheiro_do_caixa(cls):
        Registro.sub_titulo('Retirar Dinheiro do Caixa')
        valor_disponivel = 0

        for valor in cls.total_dinheiro:
            valor_disponivel += valor
            
        Registro.cor(f'Valor Disponível: R${valor_disponivel:.2f}'.replace('.',','), 'amarelo')
        print()
        
        while True:

            try:
                valor_a_ser_retirado = float(input('Digite o valor a ser retirado: R$').replace(',','.'))
                
                if 0 < valor_a_ser_retirado <= valor_disponivel:
                    
                    valor_total = 0
                    cls.total_dinheiro = [valor_disponivel - valor_a_ser_retirado]
                    
                    for valor in cls.valor_total:
                        valor_total += valor
                        x = valor_total - valor_a_ser_retirado
                        
                        cls.valor_total = [x]

                    Registro.sub_titulo('Retirar Dinheiro do Caixa')
                    nota = str(input('Adicione uma nota: ')).capitalize()
                    
                    cls.notas.append({"Valor": valor_a_ser_retirado, "Nota": nota})

                    Registro.sub_titulo('Retirar Dinheiro do Caixa')
                    Registro.cor(f'\nValor de R${valor_a_ser_retirado:.2f} retirado com sucesso'.replace(".",","), 'verde')

                    cls.valor_retirado.append(valor_a_ser_retirado)
                    break
                
                if valor_a_ser_retirado == 0:
                    Registro.sub_titulo('Retirar Dinheiro do Caixa')
                    
                    Registro.cor('Nenhum valor retirado.', 'amarelo')
                    break

                else:
                    Registro.sub_titulo('Retirar Dinheiro do Caixa')
                    Registro.cor(f'Valor Disponível: R${valor_disponivel:.2f}'.replace('.',','), 'amarelo')
                    print()

                    Registro.cor(f'O valor que deseja retirar é maior que o disponível.', 'vermelho')
                    continue
                

            except ValueError:
                Registro.sub_titulo('Retirar Dinheiro do Caixa')
                Registro.cor(f'Valor Disponível: R${valor_disponivel:.2f}'.replace('.',','), 'amarelo')
                print()
                Registro.cor('Entrada inválida. Digite apenas números', 'vermelho')
                
