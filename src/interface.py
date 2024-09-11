from limpaTela import clear
from deposito import Deposito
from rich import print

class menu_opcoes():

        # métodos
        def interface():

            while True:
                try:
                    print('*'*30)
                    print('    SEJA BEM VINDO AO LOOKBANK    ')
                    print('*'*30)

                    print('OPÇÕES: ')

                    print('1 - Extrato')
                    print('2 - Deposito')
                    print('3 - Saque')
                    print('4 - Sair')
                    
                    entrada_usuario = int(input('Digite a operação que deseja realizar: '))
            
                    if entrada_usuario == 1:
                        print(f'Extrato')
                        break
                    elif entrada_usuario == 2:
                        return Deposito().iniciar()
                    elif entrada_usuario == 3:
                        print(f'Saque')
                        break
                    elif entrada_usuario == 4:
                        print('Saindo do sistema !')
                        break  
                except ValueError as error:
                     
                     clear()
                     print('[bold red]Valor invalido ! Digite somente numero inteiro neste campo entre 1 e 4 ![/ bold red]')
                     
                     
                


                    

    
            

            
        

        
