from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

businesscards_links = db.Table('businesscards_links',
                               db.Column('businesscard_id', db.Integer, db.ForeignKey('business_cards.id'),
                                         primary_key=True),
                               db.Column('link_id', db.Integer, db.ForeignKey('links.id'), primary_key=True)
                               )


class BusinessCards(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    prefix = db.Column(db.String(10), nullable=True)
    name = db.Column(db.String(50), nullable=False)
    prename = db.Column(db.String(50), nullable=False)
    company = db.Column(db.String(100), nullable=True)
    phone = db.Column(db.String(100), nullable=True)
    email = db.Column(db.String(100), nullable=True)
    address = db.Column(db.String(100), nullable=True)
    country = db.Column(db.String(100), nullable=True)
    task = db.Column(db.String(100), nullable=True)
    picture = db.Column(db.String(100), nullable=False)
    template = db.Column(db.String(50), nullable=False)
    links = db.relationship('Links', secondary=businesscards_links, lazy='subquery',
                            backref=db.backref('businesscards', lazy=True))


class Links(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    link = db.Column(db.String(200), nullable=False)


with app.app_context():
    db.create_all()
    print("Database and tables created successfully! - 1")
    db.session.commit()

print("Database and tables created successfully! - 2")

