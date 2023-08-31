from sqlalchemy import String, Numeric, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session

# this is required by the orm
# fields shared across the objects can be set here:
#   CreatedAt
#   UpdatedAt
class Base(DeclarativeBase):
    pass

class Investment(Base):
    __tablename__ = 'investment'

    id: Mapped[int] = mapped_column(primary_key=True)
    coin: Mapped[str] = mapped_column(String(32))
    currency: Mapped[str] = mapped_column(String(3))
    amount: Mapped[float] = mapped_column(Numeric(5,2))

    def __repr__(self) -> str:
        return f"<investment coin: {self.coin}, currency: {self.currency}, amount: {self.amount}>"

engine = create_engine('sqlite:///demo_table.db')
Base.metadata.create_all(engine)

bitcoin = Investment(coin='bitcoin', currency= 'USD', amount=1.0)
ethereum = Investment(coin='ethereum', currency= 'GBP', amount=10.0)
dogecoin = Investment(coin='dogecoin', currency= 'EUR', amount=100.0)

with Session(engine) as session:
    session.add(bitcoin)
    session.add_all([ethereum, dogecoin])

    session.commit()

    stmt_all = select(Investment)
    print(stmt_all)
    all_records = session.execute(stmt_all).scalars().all()

    for record in all_records:
        print('multiple records:',record)

    stmt_bitcoin = select(Investment).where(Investment.coin == 'bitcoin')
    record = session.execute(stmt_bitcoin).scalar_one()
    print('single record:',record)

    record_by_id = session.get(Investment, 2)
    print('record_by_id:', record_by_id)

    # update within the session
    first_record = session.get(Investment, 1)
    first_record.amount = 0.756
    print(session.dirty)
    session.commit()
