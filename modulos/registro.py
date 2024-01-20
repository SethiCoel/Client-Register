import sqlite3
import os
from time import sleep
from datetime import date
from random import randint


data = date.today().strftime('%d/%m/%y')

conn = sqlite3.connect('DATABASE.db')
cursor = conn.cursor()

def gerador_de_codigo():
    while True:
        codigo = cursor.execute(f'SELECT CODIGO FROM "{data}"').fetchall()
        numero = randint(100, 999)
        if numero not in codigo:
            return numero

# cursor.execute(f'DROP TABLE "{data}"')
# cursor.execute(f'DROP TABLE "valor_{data}"')
        
cursor.execute(f'CREATE TABLE IF NOT EXISTS "{data}" (CODIGO INT PRIMARY KEY, NOME TEXT, FORMA_DE_PAGAMENTO TEXT, MENSALIDADE FLOAT, NOTAS TEXT )')
cursor.execute(f'CREATE TABLE IF NOT EXISTS "valor_{data}" (CODIGO INT PRIMARY KEY, TOTAL_DINHEIRO FLOAT , TOTAL_RETIRADO FLOAT, OUTRAS_NOTAS )')

cursor.execute(f'INSERT OR IGNORE INTO "valor_{data}" (CODIGO) VALUES ("1")')

table = cursor.execute(f'SELECT * FROM "{data}"').fetchone()

    
cursor.execute(f'UPDATE "valor_{data}" SET TOTAL_DINHEIRO = ("0") WHERE CODIGO = "1" ').fetchone()

class Registro:

    def __init__(self, cliente, forma_pagamento, mensalidade, notas):
        self._cliente = cliente
        self._forma_pagamento = forma_pagamento
        self._mensalidade = mensalidade
        self._notas = notas
        cursor.execute(f'''INSERT INTO "{data}" VALUES ("{gerador_de_codigo()}", "{self._cliente}",
                        "{self.forma_pagamento}", "{self._mensalidade}", "{self._notas}")''')
        conn.commit()
   
    def __str__(self):
        return f'{self._cliente} {self._forma_pagamento} {self._mensalidade} {self._notas}'

    def limpar_tela():
        os.system('cls')


    def listar_clientes():
        Registro.sub_titulo('Lista de clientes')
        cabecalho = (f'{"Nome do cliente":<50} {"Forma de pagamento":<25} {"Mensalidade":<20} {"Notas"}')
        print(cabecalho)
        print('-' * 135)
    	
        registros = cursor.execute(f'SELECT * FROM "{data}"').fetchall()
        if registros == []:
            print(f'{"-":<50} {"-":^18} {" " * 6} {"-":<20} {"-"}')
        
        else:
            for cliente in registros:
 
                if cliente[4] is None:
                    print(f'{cliente[1]:<50} {cliente[2]:^18} {" " * 6} {cliente[3]:<20.2f} -'.replace('.',','))
                else:
                    print(f'{cliente[1]:<50} {cliente[2]:^18} {" " * 6} {cliente[3]:<20.2f} {cliente[4]}'.replace('.',','))
                
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

    def validar_registro():
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
                opcao_escolhida = int(input('Escolha uma das opções acima. De 1 a 6: '))
                
                if 1 < opcao_escolhida > 6:
                    Registro.limpar_tela()
                    Registro.cor('Entrada inválida. Digite uma opção de 1 a 6', 'vermelho')
                    sleep(1)
                    return opcao_escolhida
                return  opcao_escolhida


            except ValueError as error:
                Registro.limpar_tela()
                Registro.cor('\nEntrada inválida. Digite apenas números', 'vermelho')
                sleep(1)
                return 7
        
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

    def fechar_caixa():
        Registro.sub_titulo('Fechar Caixa')

        valor_dinheiro = cursor.execute(f'SELECT SUM (MENSALIDADE) FROM "{data}" WHERE FORMA_DE_PAGAMENTO = "Dinheiro"').fetchone()
        valor_disponivel = cursor.execute(f'SELECT SUM (TOTAL_RETIRADO) FROM "valor_{data}" ').fetchone()


        if valor_dinheiro[0] is None or valor_disponivel[0] is None:
            print('Total Dinheiro: R$ -')
            
        else:
            print(f'Total Dinheiro: R${valor_dinheiro[0] - valor_disponivel[0]:.2f}'.replace('.',','))

        valor_pix = cursor.execute(f'SELECT SUM (MENSALIDADE) FROM "{data}" WHERE FORMA_DE_PAGAMENTO = "Pix"').fetchone()
        
        if valor_pix[0] is None or 0:
            print('Total Pix: R$ -')

        else:
            print(f'Total Pix: R${valor_pix[0]:.2f}'.replace('.',','))

        valor_deposito = cursor.execute(f'SELECT SUM (MENSALIDADE) FROM "{data}" WHERE FORMA_DE_PAGAMENTO = "Depósito"').fetchone()
       
        if valor_deposito[0] is None or 0:
            print('Total Depósito: R$ -')

        else:
            print(f'Total Depósito: R${valor_deposito[0]:.2f}'.replace('.',','))
        
        total_retirado = cursor.execute(f'SELECT SUM (TOTAL_RETIRADO) FROM "valor_{data}"').fetchone()
        
        if total_retirado[0] is None or total_retirado[0] == 0:
            Registro.cor('Total Retirado: R$ -','vermelho')
        else:
            for valor in total_retirado:

                Registro.cor(f'Total Retirado: R${valor:.2f}'.replace('.',','), 'vermelho')

        valor_total = cursor.execute(f'SELECT SUM (MENSALIDADE) FROM "{data}"').fetchone()
        
        if valor_total[0] is None or valor_disponivel[0] is None:
            Registro.cor('\nValor Total: R$ -', 'verde')
        else:
            total = valor_total[0] - valor_disponivel[0]
            Registro.cor(f'\nValor Total: R${total:.2f}'.replace('.',','), 'verde')


        print('\n')

        print(f'{"Saída":<10}        {"Notas":<50}')
        print('-' * 100)
        
        saidas = cursor.execute(f'SELECT * FROM "valor_{data}" LIMIT -1 OFFSET 1').fetchall()

        if saidas == []:
            print(f'{"-":<10}   {"-":<50}')

        else:
            for saida in saidas:
                #print(saida)
                print(f'R${saida[2]:<10.2f}      {saida[3]:<50}'.replace('.',','))
    
    
    @classmethod
    def retirar_dinheiro_do_caixa(cls):
        Registro.sub_titulo('Retirar Dinheiro do Caixa')


        soma_dinheiro = cursor.execute(f'SELECT SUM (MENSALIDADE) FROM "{data}" WHERE FORMA_DE_PAGAMENTO = "Dinheiro"').fetchone()

        if soma_dinheiro[0] is None:
            cursor.execute(f'UPDATE "valor_{data}" SET TOTAL_DINHEIRO = "0" WHERE CODIGO = "1"')
            cursor.execute(f'UPDATE "valor_{data}" SET TOTAL_RETIRADO = "0" WHERE CODIGO = "1"')
            conn.commit()
           
            valor_disponivel = cursor.execute(f'SELECT TOTAL_DINHEIRO FROM "valor_{data}" WHERE CODIGO = "1"').fetchone()
           
            for valor in valor_disponivel:
                Registro.cor(f'Valor Disponível: R${valor:.2f}'.replace('.',','), 'amarelo')
        
        else:
            valor_retirado = cursor.execute(f'SELECT SUM (TOTAL_RETIRADO) FROM "valor_{data}" ').fetchone()
            
            if valor_retirado[0] is None:

                cursor.execute(f'UPDATE "valor_{data}" SET TOTAL_DINHEIRO = ("{soma_dinheiro[0]}") WHERE CODIGO = "1"')
                
                valor_disponivel = cursor.execute(f'SELECT TOTAL_DINHEIRO FROM "valor_{data}" WHERE CODIGO = "1"').fetchone()
                
                for valor in valor_disponivel:
                    Registro.cor(f'Valor Disponível: R${valor:.2f}'.replace('.',','), 'amarelo')
            
            else:
                valor_retirado = cursor.execute(f'SELECT SUM (TOTAL_RETIRADO) FROM "valor_{data}" ').fetchone()
                
                cursor.execute(f'UPDATE "valor_{data}" SET TOTAL_DINHEIRO = ("{soma_dinheiro[0] - valor_retirado[0]}") WHERE CODIGO = "1"')
                
                conn.commit()
                
                valor_disponivel = cursor.execute(f'SELECT TOTAL_DINHEIRO FROM "valor_{data}" WHERE CODIGO = "1"').fetchone()
        
                for valor in valor_disponivel:
                    Registro.cor(f'Valor Disponível: R${valor:.2f}'.replace('.',','), 'amarelo')

        while True:

            try:
                valor_a_ser_retirado = float(input('Digite o valor a ser retirado: R$').replace(',','.'))
                
                if 0 < valor_a_ser_retirado <= valor_disponivel[0]:
                    codigos = gerador_de_codigo()
                    cursor.execute(f'INSERT INTO "valor_{data}" (CODIGO) VALUES ("{codigos}")')

                    cursor.execute(f'UPDATE "valor_{data}" SET TOTAL_RETIRADO = ("{valor_a_ser_retirado}") WHERE CODIGO = "{codigos}"')

                    cursor.execute(f'UPDATE "valor_{data}" SET TOTAL_DINHEIRO = ("{valor_retirado}") WHERE CODIGO = "1" ').fetchone()               
                
                    Registro.sub_titulo('Retirar Dinheiro do Caixa')
    
                    nota = str(input('Adicione uma nota: ')).capitalize()
                    
                    cursor.execute(f'UPDATE "valor_{data}" SET OUTRAS_NOTAS = ("{nota}") WHERE CODIGO = "{codigos}"')
                    conn.commit()

                    Registro.sub_titulo('Retirar Dinheiro do Caixa')
                    Registro.cor(f'\nValor de R${valor_a_ser_retirado:.2f} retirado com sucesso'.replace(".",","), 'verde')
                    break
                
                if valor_a_ser_retirado == 0:
                    Registro.sub_titulo('Retirar Dinheiro do Caixa')
                    Registro.cor('Nenhum valor foi retirado.', 'amarelo')
                    break
                
                if valor_a_ser_retirado == '':
                    Registro.sub_titulo('Retirar Dinheiro do Caixa')
                    Registro.cor('Nenhum valor retirado.', 'amarelo')
                    break
                
                else:
                    Registro.sub_titulo('Retirar Dinheiro do Caixa')
                    Registro.cor(f'Valor Disponível: R${valor_disponivel[0]:.2f}'.replace('.',','), 'amarelo')
                    print()

                    Registro.cor(f'O valor que deseja retirar é maior que o disponível.', 'vermelho')
                    continue
                

            except Exception as error:
                Registro.sub_titulo('Retirar Dinheiro do Caixa')
                Registro.cor(f'Valor Disponível: R${valor_disponivel[0]:.2f}'.replace('.',','), 'amarelo')
                print()
                Registro.cor(f'Entrada inválida. Digite apenas números | Error{error}', 'vermelho')
