import datetime
from app import db, ma


class Invoque(db.Model):

    __tablename__ = 'invoque'

    id = db.Column(db.Integer, primary_key=True)
    products = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    total = db.Column(db.Integer, nullable=False)
    billing_method = db.Column(db.String(255))
    billing_method = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'))

    #TODO: fix init
    def __init__(self, name, category, price, count):
        self.name = name
        self.category = category
        self.price = price
        self.count = count

    def __repr__(self):
        return f'<Invoque {self.name}>'

    def save(self):
        # if not self.id:
        db.session.add(self)
        db.session.commit()

    def update():
        db.session.commit()

    @staticmethod
    def get_all():
        return Invoque.query.filter(Invoque.state == True)

    @staticmethod
    def get_by_id(id):
        return Invoque.query.get(id)

    @staticmethod
    def get_by_name(name):
        return Invoque.query.filter_by(name=name).first()


class InvoqueSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'category', 'price', 'count', 'state')


db.create_all()
db.session.commit()