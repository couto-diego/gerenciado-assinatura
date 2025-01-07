import sys
import os

# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from sqlmodel import Session, select, func
from datetime import datetime, date
import matplotlib.pyplot as plt
from models.model import Subscription, Payment
from models.database import engine


class SubscriptionService:
    def __init__(self, engine):
        self.engine = engine

    def create(self, subscription: Subscription):
        """Cria uma nova assinatura no banco de dados."""
        with Session(self.engine) as session:
            session.add(subscription)
            session.commit()
            return subscription

    def list_all(self):
        """Lista todas as assinaturas no banco de dados."""
        with Session(self.engine) as session:
            statement = select(Subscription)
            return session.exec(statement).all()

    def delete(self, id: int):
        """Exclui uma assinatura do banco de dados pelo ID."""
        with Session(self.engine) as session:
            statement = select(Subscription).where(Subscription.id == id)
            subscription = session.exec(statement).one()
            session.delete(subscription)
            session.commit()

    def _has_payment_for_current_month(self, subscription: Subscription):
        """Verifica se a assinatura já foi paga neste mês."""
        with Session(self.engine) as session:
            statement = (
                select(Payment)
                .where(Payment.subscription_id == subscription.id)
                .where(func.extract('month', Payment.payment_date) == date.today().month)
                .where(func.extract('year', Payment.payment_date) == date.today().year)
            )
            return session.exec(statement).first() is not None

    def pay(self, subscription: Subscription):
        """Registra o pagamento de uma assinatura."""
        if self._has_payment_for_current_month(subscription):
            response = input('Essa conta já foi paga este mês. Deseja pagar novamente? (S/N): ')
            if response.upper() != 'S':
                return

        payment = Payment(subscription_id=subscription.id, payment_date=date.today())
        with Session(self.engine) as session:
            session.add(payment)
            session.commit()

    def total_value(self):
        """Retorna o valor total das assinaturas no banco de dados."""
        with Session(self.engine) as session:
            statement = select(Subscription)
            subscriptions = session.exec(statement).all()
            return sum(subscription.valor for subscription in subscriptions)

    def _get_last_12_months(self):
        """Gera uma lista dos últimos 12 meses no formato (ano, mês)."""
        today = datetime.now()
        months = [(today.year, today.month)]
        for _ in range(11):
            if today.month == 1:
                today = today.replace(year=today.year - 1, month=12)
            else:
                today = today.replace(month=today.month - 1)
            months.append((today.year, today.month))
        return months[::-1]

    def _get_values_for_months(self, last_12_months):
        """Obtém os valores das assinaturas e pagamentos para os últimos 12 meses."""
        subscription_values = []
        payment_values = []
        with Session(self.engine) as session:
            for year, month in last_12_months:
                # Valores das assinaturas no mês
                subscriptions = session.exec(
                    select(Subscription).where(Subscription.data_assinatura <= date(year, month, 1))
                ).all()
                subscription_values.append(sum(sub.valor for sub in subscriptions))

                # Valores dos pagamentos no mês
                payments = session.exec(
                    select(Payment)
                    .where(func.extract('year', Payment.payment_date) == year)
                    .where(func.extract('month', Payment.payment_date) == month)
                ).all()
                payment_values.append(
                    sum(payment.related_subscription.valor for payment in payments if payment.related_subscription)
                )

        return subscription_values, payment_values

    def gen_chart(self):
        """Gera um gráfico com os valores de assinaturas e pagamentos dos últimos 12 meses."""
        last_12_months = self._get_last_12_months()
        subscription_values, payment_values = self._get_values_for_months(last_12_months)

        if not any(subscription_values) and not any(payment_values):
            print("Não há dados suficientes para gerar o gráfico.")
            return

        months = [f"{month:02}/{year}" for year, month in last_12_months]

        plt.figure(figsize=(10, 6))
        plt.plot(months, subscription_values, label="Assinaturas", marker="o")
        plt.plot(months, payment_values, label="Pagamentos", marker="o")
        plt.xticks(rotation=45)
        plt.title("Gastos e Pagamentos nos Últimos 12 Meses")
        plt.xlabel("Meses")
        plt.ylabel("Valor (R$)")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    def list_all_payments(self):
        """Lista todos os pagamentos realizados no banco de dados."""
        with Session(self.engine) as session:
            statement = select(Payment)
            return session.exec(statement).all()

    def list_payments(self):
        """Imprime todos os pagamentos realizados no console."""
        payments = self.list_all_payments()
        if not payments:
            print("Nenhum pagamento encontrado.")
        else:
            for payment in payments:
                print(f"ID: {payment.id}, Data: {payment.payment_date}, Assinatura ID: {payment.subscription_id}")
