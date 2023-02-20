def edit_offer(cursor, offer_name, description, brand_id, car_model, price, offer_id):
    cursor.execute(f"UPDATE cars SET offer_name = ?, description = ?, car_model= ?, price = ? WHERE id = {offer_id}",
                   (offer_name, description, car_model, price))


def edit_car_brand(cursor, brand, brand_id):
    cursor.execute(f"UPDATE brands SET brand = ? WHERE id = {brand_id}", (brand,))


def edit_user(cursor, username, email, password, role):
    cursor.execute("INSERT INTO users (username, email, password, role) VALUES (?, ?, ?, ?)",
                   (username, email, password, role))


def edit_car_image(cursor, car_id, image_url):
    cursor.execute("INSERT INTO cars_images (car_id, image_url) VALUES (?, ?)",
                   (car_id, image_url))


def edit_role(cursor, role):
    cursor.execute("INSERT INTO roles (role) VALUES (?)",
                   (role,))


def edit_car_details(cursor, car_id, mileage, fuel, engine_capacity, doors, gas=0):
    cursor.execute("INSERT INTO cars_details VALUES (?, ?, ?, ?, ?, ?)",
                   (car_id, mileage, fuel, engine_capacity, doors, gas))
