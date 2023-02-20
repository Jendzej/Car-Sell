def get_offer_by_id(conn, car_id):
    return conn.execute(f'SELECT * FROM cars WHERE id = {car_id}').fetchone()


def get_all_offers(conn):
    return conn.execute('SELECT * FROM cars').fetchall()


def get_offer_details(conn, car_id):
    return conn.execute(f'SELECT * FROM cars_details WHERE car_id = {car_id}').fetchone()


def get_offer_images(conn, car_id):
    return conn.execute(f"SELECT image_url FROM cars_images WHERE car_id = {car_id}").fetchall()


def get_car_brand(conn, brand_id):
    return conn.execute(f"SELECT brand FROM brands WHERE id = {brand_id}").fetchone()[0]
