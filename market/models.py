from market import db, login_manager
from market import bcrypt
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# WARNING : after creating your model you should go in a Python shell and type
# 'from market.models import db' then 'db.create_all()'.
# Market being the value of __name__. This creates an SQL db.
# To play around import the classes herein in the python cmd line.
class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email_address = db.Column(db.String(length=50),
                              nullable=False,
                              unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)
    budget = db.Column(db.Integer(), nullable=False, default=1000)
    items = db.relationship('Item', backref='owned_user', lazy=True)

    @property
    def prettier_budget(self):
        if len(str(self.budget)) >= 4:
            number_with_commas = "{:,}".format(self.budget)
            return number_with_commas
        else:
            return self.budget

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(
            plain_text_password).decode('utf-8')

    def check_password_connection(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash,
                                          attempted_password)


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


# sample query with sqlAlchemy item1.owner = User.query.filter_by(username='JC').first().id