
class Cliente:
    def __init__(self, nome):
        self.nome = nome

    def cadastro(self):
        self.telefone = telefone
        self.conta = conta


class Conta:
    saldo = 0
    limite = 0
    oper = str
    valor = 0
    historico = dict(oper=oper, valor=valor)

    def __init__(self, conta):
        self.conta = conta
        self.saldo = saldo
        self.limite = limite
        self.saldo_lim = limite

    def conta(self, conta, cliente):
        self.conta = conta
        self.cliente = cliente
        return Cliente.cadastro.conta(conta)

    def saldo(self, conta):
        return saldo

    def credito_conta(self, conta, valor):
        saldo = saldo + valor

    def debito_conta(self, conta, valor):
        saldo = saldo - valor

    def limite(self, conta, limite):
        self.conta = conta
        self.limite = limite
        return limite

    def saldo_lim(self, conta):
        return saldo_lim

    def debito_lim(self, conta, valor):
        saldo_lim = saldo_lim - valor

    def acerto_lim(self, conta, valor):
        saldo_lim = saldo_lim + valor

    def historico(self, conta, oper, valor):
        historico.append(oper, valor)

    def extrato(self):
        print("Extrato CC No "+conta)
        for oper in historico:

            print(historico['oper']+"            "+historico['valor'])
        print("     Saldo            "+saldo)
        print("    Limite            "+limite)
        print("Disponivel            "+saldo+saldo_lim)


class Oper:
    x = 0

    def saque(self, conta, valor):
        if valor < Conta.saldo(conta):
            Conta.credito_conta(conta, valor)
            print("Saque efetuado com Sucesso")

        elif valor < Conta.saldo(conta) + Conta.saldo_lim(conta):
            x = valor - Conta.saldo(conta)
            Conta.debito_conta(conta, Conta.saldo(conta))
            Conta.debito_lim(conta, x)
            print("Saque efetuado com Sucesso")

        else:
            print("Saldo Insuficiente")

    def deposito(self, valor, conta):
        if Conta.saldo_lim(conta) < Conta.limite(conta):
            if valor < Conta.limite(conta) - Conta.saldo_lim(conta):
                Conta.acerto_lim(conta, valor)
                print("Deposito Efetuado")

            else:
                x = 0
                y = 0
                x = valor - (Conta.limite(conta) - Conta.saldo_lim(conta))
                y = valor - x
                Conta.acerto_lim(conta, x)
                Conta.credito_conta(conta, y)
                print("Deposito Efetuado")
        else:
            Conta.credito_conta(conta, valor)
            print("Deposito Efetuado")


def main():
    clientes = []
    contas = {}

    print("Sistema Bancario")

    menu = {}
    menu['1'] = "Cadastrar Cliente"
    menu['2'] = "Abrir Conta"
    menu['3'] = "Movimentar Conta"
    menu['4'] = "Extrato"
    menu['5'] = "Sair"

    while True:
        opcao = menu.keys()
        for entrada in opcao:
            print(entrada, menu[entrada])

        selecao = input("Selecione a Opção:")
        if selecao == '1':
            cliente = input('Digite o nome do Cliente:')
            if cliente in clientes:
                print('Cliente já cadastrado')
            else:
                clientes.append(cliente)
                cliente = Cliente(cliente)

                telefone = input('Digite o Telefone do Cliente:')
                cliente.telefone = telefone

            input('Cliente Cadastrado. Pressione Enter para continuar')

        elif selecao == '2':
            print('Digite o nome do Cliente')
            cliente = input()
            if cliente in clientes:
                print('Digite o numero de conta a ser cadastrado para o cliente')
                cod = input()
                if cod in contas:
                    print('Conta já cadastrada')
                    input('Pressione Enter para retornar')
                else:
                    print('Deseja atribuir um limite a conta? S/N')
                    resp = input()
                    if resp == 'N'or'n':
                        contas = dict(cod=cod, nome=cliente)
                        Conta.conta(cod, cod, cliente)
                        print('Conta cadastrada com sucesso')
                    elif resp == 'S'or's':
                        print('Digite o valor do Limite:')
                        lim = input()
                        contas = dict(cod=cod, nome=cliente)
                        Conta.conta(cod, cod, cliente)
                        Conta.limite(cod, lim)
                        print('Conta cadastrada com sucesso')
                    else:
                        print("Opção Invalida")
            else:
                print('Cliente não cadastrado')
                input('Pressione Enter para retornar')

        elif selecao == '3':
            menu = {}
            menu['1'] = "Efetuar Depósito"
            menu['2'] = "Efetuar Saque"

            while True:
                opcao = menu.keys()
                for entrada in opcao:
                    print(entrada, menu[entrada])

                selecao = input("Selecione a Opção:")
                if selecao == '1':
                    print('Digite o numero da conta:')
                    conta = input()
                    if conta in contas:
                        cliente = contas['nome']
                        print('Digite o valor a ser depositado:')
                        valor = int(input())
                        Oper.deposito(valor, conta)
                        Conta.historico(conta, 'Deposito', valor)
                        input('Pressione Enter para retornar ao Menu')
                    else:
                        print('Conta Não Cadastrada')

                elif selecao == '2':
                    print('Digite o numero da conta:')
                    conta = input()
                    if conta in contas:
                        cliente = contas['nome']
                        print('Digite o valor do Saque:')
                        valor = int(input())
                        Oper.saque(conta, valor)
                        Conta.historico(conta, 'Saque', valor)
                        input('Pressione Enter para retornar ao Menu')
                    else:
                        print('Conta Não Cadastrada')

                else:
                    print('Opção Invalida')
                    break

        elif selecao == '4':
            print('Digite o numero da conta:')
            conta = input()
            if conta in contas:
                cliente = contas['nome']
                Conta.extrato(conta)
            else:
                print('Conta Não Cadastrada')

        elif selecao == '5':
            break

        else:
            print("Opção Invalida")


main()
