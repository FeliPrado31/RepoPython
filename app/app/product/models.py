from app import db, ma


class Product(db.Model):

    __tablename__ = 'product'

    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(80), nullable=False)
    name = db.Column(db.String(256), unique=True, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    count = db.Column(db.Integer, nullable=False)
    state = db.Column(db.Boolean, default=True)

    def __init__(self, name, category, price, count, state):
        self.name = name
        self.category = category
        self.price = price
        self.count = count
        self.state = state

    def __repr__(self):
        return f'<Product {self.name}>'

    def save(self):
        # if not self.id:
        db.session.add(self)
        db.session.commit()

    def update():
        db.session.commit()

    @staticmethod
    def get_all():
        return Product.query.all()

    @staticmethod
    def get_by_id(id):
        return Product.query.get(id)

    @staticmethod
    def get_by_name(name):
        return Product.query.filter_by(name=name).first()


class ProductSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'category', 'price', 'count', 'state')
