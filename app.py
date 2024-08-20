from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from flask_sqlalchemy import SQLAlchemy
import qrcode
from io import BytesIO
import base64
import os

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


@app.route('/')
def index():
    cards = BusinessCards.query.all()
    return render_template('index.html', cards=cards)


@app.route('/create', methods=['GET', 'POST'])
def create_card():
    if request.method == 'POST':
        picture_file = request.files['picture']
        picture_filename = picture_file.filename
        picture_file.save(os.path.join('static/images', picture_filename))

        card = BusinessCards(
            prefix=request.form.get('prefix'),
            name=request.form['name'],
            prename=request.form['prename'],
            company=request.form.get('company'),
            phone=request.form.get('phone'),
            email=request.form.get('email'),
            address=request.form.get('address'),
            country=request.form.get('country'),
            task=request.form.get('task'),
            picture=picture_filename,
            template=request.form['template']
        )

        for link_name, link_url in zip(request.form.getlist('link_name'), request.form.getlist('link_url')):
            if link_name and link_url:
                link = Links(name=link_name, link=link_url)
                card.links.append(link)

        db.session.add(card)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('create.html')


if __name__ == '__main__':
    app.run()
