def add_offer(cursor, user_id, offer_name, description, brand_id, car_model, price):
    cursor.execute(
        "INSERT INTO cars (user_id, offer_name, description, brand_id, car_model, price) VALUES (?, ?, ?, ?, ?, ?)",
        (user_id, offer_name, description, brand_id, car_model, price))


def add_car_brand(cursor, brand):
    cursor.execute("INSERT INTO brands (brand) VALUES (?)",
                   (brand,))


def add_user(cursor, username, email, password, role):
    cursor.execute("INSERT INTO users (username, email, password, role) VALUES (?, ?, ?, ?)",
                   (username, email, password, role))


def add_car_image(cursor, car_id, image_url):
    cursor.execute("INSERT INTO cars_images (car_id, image_url) VALUES (?, ?)",
                   (car_id, image_url))


def add_role(cursor, role):
    cursor.execute("INSERT INTO roles (role) VALUES (?)",
                   (role,))


def add_car_details(cursor, car_id, mileage, fuel, engine_capacity, doors, gas=0):
    cursor.execute("INSERT INTO cars_details VALUES (?, ?, ?, ?, ?, ?)",
                   (car_id, mileage, fuel, engine_capacity, doors, gas))
