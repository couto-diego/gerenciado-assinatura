from sqlmodel import SQLModel, Field, Relationship
from typing import List, Optional
from datetime import date

class Subscription(SQLModel, table=True):
    """
    Representa uma assinatura de serviço.
    """
    id: Optional[int] = Field(default=None, primary_key=True)
    empresa: str = Field(nullable=False)  # Nome da empresa do serviço (ex: Netflix, Amazon)
    data_assinatura: date = Field(nullable=False)  # Data em que a assinatura foi realizada
    valor: float = Field(nullable=False)  # Valor mensal da assinatura

    # Relacionamento com pagamentos
    payments: List["Payment"] = Relationship(
        back_populates="related_subscription",
        sa_relationship_kwargs={"cascade": "all, delete-orphan"}
    )

    def __repr__(self):
        return f"<Subscription(id={self.id}, empresa='{self.empresa}', valor={self.valor:.2f})>"

class Payment(SQLModel, table=True):
    """
    Representa um pagamento realizado para uma assinatura.
    """
    id: Optional[int] = Field(default=None, primary_key=True)
    subscription_id: int = Field(foreign_key="subscription.id", nullable=False)
    payment_date: date = Field(nullable=False)  # Data do pagamento

    # Relacionamento com assinatura
    related_subscription: Subscription = Relationship(back_populates="payments")

    def __repr__(self):
        return f"<Payment(id={self.id}, subscription_id={self.subscription_id}, date={self.payment_date})>"

