import datetime
from app import db, ma


class Invoque(db.Model):

    __tablename__ = 'invoque'

    id = db.Column(db.Integer, primary_key=True)
    products = db.Column(db.String(255), nullable=False)
    total = db.Column(db.Integer, nullable=False)
    num_products = db.Column(db.Integer, nullable=False)
    billing_method = db.Column(db.String(255))
    time_buy = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    client_id = db.Column(db.Integer, nullable=False)

    def __init__(self, products, total, billing_method, client_id, num_products, time_buy):
        self.products = products
        self.billing_method = billing_method
        self.time_buy = time_buy
        self.client_id = client_id
        self.num_products = num_products
        self.total = total

    def __repr__(self):
        return f'<Invoque {self.client_id}>'

    def save(self):
        # if not self.id:
        db.session.add(self)
        db.session.commit()

    def update():
        db.session.commit()

    @staticmethod
    def get_all():
        return Invoque.query.all()

    @staticmethod
    def get_by_id(id):
        return Invoque.query.get(id)

    @staticmethod
    def get_by_name(name):
        return Invoque.query.filter_by(name=name).first()


class InvoqueSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'products',
                  'billing_method', 'client_id', 'total', 'time_buy', 'num_products')


db.create_all()
db.session.commit()
