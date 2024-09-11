from rich import print
import app
from limpaTela import clear

class Deposito:
    def __init__(self):
        self.saldo = 0  

    def depositar(self, valor):
        if valor > 15000000:
            print('[bold red]O valor não pode exceder R$150.000,00, tente novamente![/bold red]')
            return False
        elif valor <= 0:
            print('[bold red]O valor deve ser maior que R$0,00, tente novamente![/bold red]')
            return False
        else:
            self.saldo += valor 
            return True

    def mostrar_extrato(self):
        print('*' * 30)
        print('           EXTRATO   ')
        print('*' * 30)
        print('LANÇAMENTOS:')
        print('-' * 30)
        print(f'DEPÓSITO ATM | SALDO: R${self.saldo:.2f}')
        print('             |      |')
        print('             |      |')
        print('-' * 30)
        print(f'               [bold green]SALDO: R${self.saldo:.2f}[/bold green]')
        print('-' * 30)
        print('        FIM DO EXTRATO     ')
        print('-' * 30)

    def iniciar(self):
        while True:
            try:
                valor = int(input('Qual o valor que deseja depósitar? '))
                if self.depositar(valor):  # Tenta depositar o valor
                    while True:
                        nova_operacao = input('Deseja realizar uma nova operação (s/n): ').lower()
                        if nova_operacao == 's':
                            valor = int(input('Qual o valor que deseja depósitar? '))
                            break  # Reinicia o processo de depósito
                        elif nova_operacao == 'n':
                            self.mostrar_extrato()
                            print('Sistema encerrando ...')
                            clear()
                            return app.menu_opcoes.interface()
                        else:
                            print('[bold red]Opção inválida! Por favor, escolha "s" ou "n".[/bold red]')
            except ValueError:
                print('[bold red]O campo só aceita números inteiros, por favor tente novamente![/bold red]')

