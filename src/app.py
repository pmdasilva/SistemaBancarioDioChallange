from rich  import print
import os

class Atm():
  def __init__(self):
    # Attributes
    self.saldo = 0
    self.valor_usuario = 0
    self.tentaivas = 3
    self.limite_saque = 500
    self.valor_depositado = 0  
    self.valor_saque = 0       



  #methods
  clear = lambda:os.system('cls')

  def opcao_inicializacao(self):
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

            self.entrada_usuario = int(input('Digite a operação que deseja realizar: '))

            if self.entrada_usuario == 1:
                return self.mostrar_extrato()
            elif self.entrada_usuario == 2:
                return self.depositar()
            elif self.entrada_usuario == 3:
                return self.sacar()
            elif self.entrada_usuario == 4:
                print('Saindo do sistema !')
                break
        except ValueError as error:
              print(f'[bold red]Valor invalido ! Digite somente numero inteiro neste campo entre 1 e 4 ![/ bold red]')


  def sacar(self):
    while True:
      try:
        self.valor_saque = int(input('Qual o valor que deseja sacar ?'))
        if self.valor_saque > 500:
          print(f'[bold red]O sistema não permite saques maiores de R$500.00, tente novamente ![/bold red]')
        elif self.valor_saque > self.saldo:
          print(f'[bold red]Não possivél sacar o valor ! Saldo insuficiente ![/bold red]')
          print(f'[bold red]Saldo disponivel para o saque: R${self.saldo}[/bold red]')
          clear()
          return self.opcao_inicializacao()
          break
        elif self.valor_saque <= 0:
          print('[bold red]O valor não pode ser sacado ! tente novamente com um valor acima de R$0.00,  minimo R$1 ![/bold red]')
        else:
          self.saldo -= self.valor_saque
          print(f'[bold green]O valor foi sacado com sucesso ! Valor sacado foi de  R${self.valor_saque}[/bold green]')
          print(f'[bold green]Valor disponivel em conta R${self.saldo}[/bold green]')
          print('*' * 30)
          print('           EXTRATO   ')
          print('*' * 30)
          print('LANÇAMENTOS:')
          print('-' * 30)
          print(f'VALOR SACADo ATM | SALDO: R${self.valor_saque:.2f}')
          print('             |      |')
          print('             |      |')
          print('-' * 30)
          print(f'               [bold green]SALDO: R${self.saldo:.2f}[/bold green]')
          print('-' * 30)
          print('        FIM DO EXTRATO     ')
          print('-' * 30)
          return self.opcao_inicializacao()
      except ValueError:
        print('[red]Insira somente numeros inteiros ![/red]')


  def depositar(self):
    while True:
      try:
        self.valor_depositado = int(input('Qual o valor que deseja depositar ?'))
        if self.valor_depositado <= 0:
          print('[bold red]O valor não pode ser depositado ! tente novamente com um valor acima de R$0.00 ![/bold red]')
        else:
          self.saldo += self.valor_depositado
          print(f'[bold green]O valor foi Depositado com sucesso com sucesso ! Valor depositado foi de  R${self.valor_depositado}[/bold green]')
          print(f'[bold green]Valor disponivel em conta R${self.saldo}[/bold green]')
          # def mostrar_extrato_deposito(self):
          print('*' * 30)
          print('           EXTRATO   ')
          print('*' * 30)
          print('LANÇAMENTOS:')
          print('-' * 30)
          print(f'DEPÓSITO ATM | SALDO: R${self.valor_depositado:.2f}')
          print('             |      |')
          print('             |      |')
          print('-' * 30)
          print(f'               [bold green]SALDO: R${self.saldo:.2f}[/bold green]')
          print('-' * 30)
          print('        FIM DO EXTRATO     ')
          print('-' * 30)
          return self.opcao_inicializacao()
      except ValueError:
        print('[red]Insira somente numeros inteiros ![/red]')


  def mostrar_extrato(self):
    while True:
      try:
        print('*' * 30)
        print('           EXTRATO   ')
        print('*' * 30)
        print('ULTIMOS LANÇAMENTOS:')
        print('-' * 30)
        print(f'DEPÓSITO ATM | SALDO: R${self.valor_depositado:.2f}')
        print(f'SAQUE    ATM | SALDO: R${self.valor_saque:.2f}')
        print(f'VALOR DISP. ATM | SALDO: R${self.saldo:.2f}')
        print('             |      |')
        print('             |      |')
        print('-' * 30)
        print(f'               [bold green]SALDO: R${self.saldo:.2f}[/bold green]')
        print('-' * 30)
        print('        FIM DO EXTRATO     ')
        print('-' * 30)
        return self.opcao_inicializacao()
      except ValueError:
        print('Algo ocorreu de errado tente novamente !')





atm = Atm()
atm.opcao_inicializacao()