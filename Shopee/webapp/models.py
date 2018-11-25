from webapp import db

# ORM for exchange rate table in mysql
class ExchangeRate(db.Model):
    __tablename__ = 'exchange_rates'

    from_country = db.Column(db.String(30), primary_key=True, nullable=False)
    to_country = db.Column(db.String(30), primary_key=True, nullable=False)
    date = db.Column(db.String(10),primary_key=True,nullable=False,index=True)
    rate = db.Column(db.DECIMAL, nullable=True)

