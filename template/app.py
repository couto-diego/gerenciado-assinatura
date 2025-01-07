import sys
import os
from datetime import datetime
from decimal import Decimal

# Adiciona o diretório raiz ao caminho de importação
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.database import init_db, engine
from models.model import Subscription, Payment  # Corrigido para 'Payment'
from views.view import SubscriptionService


class UI:
    def __init__(self):
        """Inicializa o serviço de assinaturas."""
        self.subscription_service = SubscriptionService(engine)

    def add_subscription(self):
        """Adiciona uma nova assinatura ao banco de dados."""
        try:
            empresa = input('Empresa: ')

            # Valida e processa a data de assinatura
            while True:
                try:
                    data_input = input('Data de assinatura (dd/mm/yyyy): ')
                    data_assinatura = datetime.strptime(data_input, '%d/%m/%Y')
                    break
                except ValueError:
                    print("Data inválida. Por favor, insira no formato dd/mm/yyyy.")

            # Valida e processa o valor da assinatura
            while True:
                try:
                    valor_input = input('Valor: ')
                    valor = Decimal(valor_input)
                    break
                except Exception:
                    print("Valor inválido. Insira um número válido.")

            subscription = Subscription(
                empresa=empresa, data_assinatura=data_assinatura, valor=valor
            )
            self.subscription_service.create(subscription)
            print('Assinatura adicionada com sucesso.')
        except Exception as e:
            print(f'Erro ao adicionar assinatura: {e}')

    def delete_subscription(self):
        """Remove uma assinatura do banco de dados."""
        try:
            subscriptions = self.subscription_service.list_all()
            if not subscriptions:
                print('Nenhuma assinatura encontrada para excluir.')
                return

            print('Escolha qual assinatura deseja excluir:')
            for subscription in subscriptions:
                print(f'[{subscription.id}] -> {subscription.empresa}')

            # Valida o ID selecionado
            while True:
                try:
                    choice = int(input('Digite o ID da assinatura: '))
                    if not any(sub.id == choice for sub in subscriptions):
                        print("ID inválido. Tente novamente.")
                    else:
                        break
                except ValueError:
                    print("Por favor, insira um número válido.")

            self.subscription_service.delete(choice)
            print('Assinatura excluída com sucesso.')
        except Exception as e:
            print(f'Erro ao excluir assinatura: {e}')

    def pay_subscription(self):
        """Marca uma assinatura como paga."""
        try:
            subscriptions = self.subscription_service.list_all()
            if not subscriptions:
                print('Nenhuma assinatura encontrada para pagar.')
                return

            print('Escolha qual assinatura deseja pagar:')
            for subscription in subscriptions:
                print(f'[{subscription.id}] -> {subscription.empresa}')

            # Valida o ID selecionado
            while True:
                try:
                    choice = int(input('Digite o ID da assinatura para pagar: '))
                    if not any(sub.id == choice for sub in subscriptions):
                        print("ID inválido. Tente novamente.")
                    else:
                        break
                except ValueError:
                    print("Por favor, insira um número válido.")

            subscription = next(sub for sub in subscriptions if sub.id == choice)
            self.subscription_service.pay(subscription)
            print(f'Pagamento registrado para a assinatura da empresa: {subscription.empresa}.')
        except Exception as e:
            print(f'Erro ao registrar pagamento: {e}')

    def total_value(self):
        """Exibe o valor total mensal de todas as assinaturas."""  
        try:
            total = self.subscription_service.total_value()
            print(f'Seu valor total mensal em assinaturas: R$ {total:.2f}')
        except Exception as e:
            print(f'Erro ao calcular valor total: {e}')

    def display_menu(self):
        """Exibe o menu de opções para o usuário."""
        print('''\nMenu:
[1] -> Adicionar assinatura
[2] -> Remover assinatura
[3] -> Valor total
[4] -> Gastos últimos 12 meses (gerar gráfico)
[5] -> Realizar pagamento
[6] -> Sair''')

    def start(self):
        """Inicia o loop principal do programa."""
        while True:
            self.display_menu()
            try:
                choice = int(input('Escolha uma opção: '))
                if choice not in range(1, 7):
                    print('Opção inválida. Tente novamente.')
                    continue

                if choice == 1:
                    self.add_subscription()
                elif choice == 2:
                    self.delete_subscription()
                elif choice == 3:
                    self.total_value()
                elif choice == 4:
                    self.subscription_service.gen_chart()
                elif choice == 5:
                    self.pay_subscription()
                elif choice == 6:
                    print('Encerrando o programa.')
                    break
            except ValueError:
                print('Entrada inválida. Por favor, insira um número.')
            except Exception as e:
                print(f"Erro: {e}. Certifique-se de que os dados estão corretos.")


if __name__ == '__main__':
    # Inicializa o banco de dados (criação das tabelas)
    init_db()
    UI().start()
