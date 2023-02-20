import sqlite3

from flask import Flask, render_template, request, flash, redirect, url_for
from werkzeug.exceptions import abort

from database.queries.fetch import *
from database.queries.insert import *

app = Flask(__name__)
app.config['SECRET_KEY'] = "password"


def get_db_connection():
    conn = sqlite3.connect('database/database.db')
    conn.row_factory = sqlite3.Row
    return conn


def get_cars_images(conn, car_id):
    return conn.execute(f"SELECT image_url FROM cars_images WHERE car_id = {car_id}").fetchall()


@app.route('/')
def index():
    conn = get_db_connection()
    cars = conn.execute('SELECT * FROM cars').fetchall()
    all_offers = []
    for x in cars:
        all_offers.append({
            "id": x["id"],
            "added": x["added"],
            "offer_name": x["offer_name"],
            "description": x["description"],
            "car_model": x["car_model"],
            "price": x["price"],
            "brand": conn.execute(f'SELECT brand FROM brands WHERE id = {x["brand_id"]}').fetchone()[0],
            "car_images": get_cars_images(conn, x["id"])
        })
    conn.close()
    return render_template("home.html", cars=all_offers)


def get_car_offer(car_id):
    conn = get_db_connection()
    offer = get_offer_by_id(conn, car_id)
    brand = get_car_brand(conn, offer["brand_id"])
    car_images = get_offer_images(conn, car_id)
    offer_details = get_offer_details(conn, car_id)
    conn.close()
    if offer is None:
        abort(404)
    return offer, car_images, brand, offer_details


@app.route('/<int:car_id>')
def car_offer(car_id):
    offer, car_images, brand, offer_details = get_car_offer(car_id)
    return render_template('offer.html', offer=offer, car_images=car_images, brand=brand, details=offer_details)


@app.route('/create', methods=['GET', 'POST'])
def create_offer():
    if request.method == 'POST':
        offer_name = request.form['offer_name']
        description = request.form['description']
        brand_id = request.form['brand_id']
        price = request.form['price']
        car_model = request.form['car_model']
        user_id = request.form['user_id']

        if not offer_name or not description or not brand_id:
            flash("Everything required!")
        else:
            conn = get_db_connection()
            add_offer(conn, user_id, offer_name, description, brand_id, car_model, price)
            conn.commit()
            conn.close()
            return redirect(url_for('index'))
    return render_template('create.html')


@app.route('/<int:car_id>/edit', methods=['GET', 'POST'])
def edit_offer(car_id):
    car = get_car_offer(car_id)
    if request.method == 'POST':
        offer_name = request.form['offer_name']
        description = request.form['description']
        price = request.form['price']
