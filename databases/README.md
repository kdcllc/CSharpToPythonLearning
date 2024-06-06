# Databases with SQLAlchemy ORM

This guide will help you get started with using Python and SQLAlchemy ORM to interact with databases. If you are coming from a C# background and are familiar with Entity Framework, you will find many similarities in concepts and structure.

## Prerequisites

- Python 3.x installed on your machine
- Basic understanding of Python programming

## Installation

First, you need to install SQLAlchemy. You can do this using pip:

```bash
pip install sqlalchemy
```

## Files Overview

### demo-orm-table.py

This script demonstrates how to create a single table and perform basic CRUD (Create, Read, Update, Delete) operations.

### demo-orm-tables.py

This script demonstrates how to create multiple tables with relationships between them and perform basic CRUD operations.

## Running the Scripts

### Single Table Example

To run the single table example, execute the following command:

```bash
python demo-orm-table.py
```

This script will:

1. Create a table named `investment`.
2. Insert three records into the table.
3. Query all records and print them.
4. Query a single record by a specific condition and print it.
5. Update a record and print the updated record.

### Multiple Tables Example

To run the multiple tables example, execute the following command:

```bash
python demo-orm-tables.py
```

This script will:

1. Create two tables named `portfolio` and `investment`.
2. Insert records into both tables and establish relationships between them.
3. Query a portfolio and print its investments.

## Detailed Explanation

### demo-orm-table.py

```python
from sqlalchemy import String, Numeric, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session

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

    first_record = session.get(Investment, 1)
    first_record.amount = 0.756
    print(session.dirty)
    session.commit()
```

### demo-orm-tables.py

```python
from typing import List
from sqlalchemy import ForeignKey, String, Numeric, Text, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session, relationship

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
```

## Conclusion

This guide provides a basic introduction to using SQLAlchemy ORM with Python. For more advanced usage and features, refer to the [SQLAlchemy documentation](https://docs.sqlalchemy.org/).

### Key Differences from Entity Framework

- **Configuration**: In SQLAlchemy, you configure your database connection using `create_engine`, whereas in Entity Framework, you typically use a connection string in a configuration file.
- **Models**: SQLAlchemy models are defined using Python classes with mapped columns, similar to how you define models in Entity Framework using C# classes with data annotations or Fluent API.
- **Sessions**: SQLAlchemy uses sessions to manage transactions, similar to how Entity Framework uses `DbContext`.
- **Queries**: SQLAlchemy queries are constructed using a query builder pattern, similar to LINQ in Entity Framework.

By understanding these key differences and similarities, you should be able to transition smoothly from Entity Framework to SQLAlchemy.
