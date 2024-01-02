from typing import List
from sqlalchemy import ForeignKey, String, Numeric, Text, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session, relationship

# this is required by the orm
# fields shared across the objects can be set here:
#   CreatedAt
#   UpdatedAt
class Base(DeclarativeBase):
    pass

class Portfolio(Base):
    __tablename__ = "portfolio"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(256))
    description: Mapped[str] = mapped_column(Text())
    
    investments: Mapped[List['Investment']] = relationship(back_populates='portfolio')

    def __repr__(self) -> str:
        return f"<Portfolio name: {self.name} with {len(self.investments)} investment(s)>"
    
class Investment(Base):
    __tablename__ = 'investment'

    id: Mapped[int] = mapped_column(primary_key=True)
    coin: Mapped[str] = mapped_column(String(32))
    currency: Mapped[str] = mapped_column(String(3))
    amount: Mapped[float] = mapped_column(Numeric(5,2))

    portfolio_id: Mapped[int] = mapped_column(ForeignKey('portfolio.id'))
    portfolio: Mapped['Portfolio'] = relationship(back_populates='investments')
    def __repr__(self) -> str:
        return f"<investment coin: {self.coin}, currency: {self.currency}, amount: {self.amount}>"

engine = create_engine('sqlite:///demo_tables.db')
Base.metadata.create_all(engine)

bitcoin = Investment(coin='bitcoin', currency= 'USD', amount=1.0)
ethereum = Investment(coin='ethereum', currency= 'GBP', amount=10.0)
dogecoin = Investment(coin='dogecoin', currency= 'EUR', amount=100.0)

portfolio_1 = Portfolio(name='Portfolio 1', description='Desc 1')
portfolio_2 = Portfolio(name='Portfolio 2', description='Desc 2')

bitcoin.portfolio = portfolio_1

portfolio_2.investments.extend([ethereum, dogecoin])

with Session(engine) as session:
    session.add(bitcoin)
    session.add(portfolio_2)
    session.commit()

    portfolio = session.get(Portfolio, 2)
    for investment in portfolio.investments:
        print(investment)
