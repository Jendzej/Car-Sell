import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cursor = connection.cursor()
cursor.execute("INSERT INTO brands (brand) VALUES (?)",
               ("Audi",))
cursor.execute("INSERT INTO cars (offer_name, description, brand_id, car_model, price)  VALUES (?, ?, ?, ?, ?)",
               ("Audi a3 cheap! occasion", "Very good car, please someone buy it!", 1, "a3", 15090.99))
cursor.execute("INSERT INTO cars_images (car_id, image_url) VALUES (?, ?)",
               (1, "https://cdn.proxyparts.com/vehicles/100012/6620067/large/3501ad31-7649-476b-a779-080936e33614.jpg"))
connection.commit()
connection.close()
