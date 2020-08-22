from app import db, ma


class Client(db.Model):

    __tablename__ = 'client'

    id = db.Column(db.Integer, primary_key=True)
    cc = db.Column(db.String(80), nullable=False)
    name = db.Column(db.String(256), unique=True, nullable=False)
    address = db.Column(db.String(256), unique=True, nullable=False)
    telephone = db.Column(db.String(10), nullable=False)
    photo = db.Column(db.Text, nullable=False)

    def __init__(self, name, cc, telephone, photo, address):
        self.name = name
        self.cc = cc
        self.telephone = telephone
        self.photo = photo
        self.address = address

    def __repr__(self):
        return f'<client {self.name}>'

    def save(self):
        # if not self.id:
        db.session.add(self)
        db.session.commit()

    def update():
        db.session.commit()

    @staticmethod
    def get_by_id(id):
        return Client.query.get(id)

    @staticmethod
    def get_by_name(name):
        return Client.query.filter_by(name=name).first()


class ClientSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'cc', 'telephone', 'address')
