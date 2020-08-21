from app import db


class User(db.Model):

    __tablename__ = 'product'

    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(80), nullable=False)
    name = db.Column(db.String(256), unique=True, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    count = db.Column(db.Integer, nullable=False)
    state = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return f'<Product {self.name}>'

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_by_id(id):
        return User.query.get(id)

    @staticmethod
    def get_by_name(name):
        return User.query.filter_by(name=name).first()
