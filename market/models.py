from market import db


# WARNING : after creating your model you should go in a Python shell and type
# 'from market import db' then 'db.create_all()'.
# Market being the value of __name__. This creates an SQL db.
class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email_address = db.Column(db.String(length=50),
                              nullable=False,
                              unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)
    budget = db.Column(db.Integer(), nullable=False, default=1000)
    items = db.relationship('Item', backref='owned_user', lazy=True)


# backref='owned_user'
# Used for tracing back the owner of the item that is being purchased
# since we'll be making a link between a User item and an Item item.
# lazy=True
# tells SQLAlchemy to grab all the items in one go.
class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=1024),
                            nullable=False,
                            unique=True)
    owner = db.Column(db.Integer(), db.ForeignKey('user.id'))

    def __repr__(self):
        return f'Item {self.name}'
