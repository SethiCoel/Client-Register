from modulos.registro import Registro
from time import sleep



def exibir_nome_programa():
    Registro.limpar_tela()
    Registro.cor('=' * 30, 'ciano')

    Registro.cor(f'{"Cliente Register":^30}', 'ciano')

    Registro.cor('=' * 30, 'ciano')

def menu_de_opcoes():
    print('''
(1) Registrar novo cliente
(2) Listar clientes
(3) Retirar dinheiro do caixa 
(4) Fechar caixa      
(5) Sair          
          ''')

def voltar_ao_menu():
    input('\nPressione ENTER para voltar.')
    main()

def escolher_opcoes():
    opcao = Registro.validar_opcao_escolhida()
    
    if opcao == 1:
        Registro.validar_registro()
        voltar_ao_menu()

    elif opcao == 2:
        Registro.listar_clientes()
        voltar_ao_menu()
    
    elif opcao == 3:
        Registro.retirar_dinheiro_do_caixa()
        voltar_ao_menu()

    elif opcao == 4:
        Registro.fechar_caixa()
        voltar_ao_menu()

    
    elif opcao == 5:
        Registro.encerrar_programa()

    else:
        main()

def main():
    
    exibir_nome_programa()
    menu_de_opcoes()
    escolher_opcoes()

if __name__ == '__main__':
    main()
