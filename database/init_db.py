import sqlite3

from database.queries.insert import add_offer, add_car_details, add_role, add_user, add_car_brand, add_car_image

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cursor = connection.cursor()
add_car_brand(cursor, "Audi")
add_car_brand(cursor, "BWM")
add_role(cursor, "user")
add_role(cursor, "admin")
add_user(cursor, "username", "email", "password", "user")
add_offer(cursor, 1, "Audi a3 cheap! occassion 2.0", "Very good car, please someone buy it!", 1, "a3", 15090.99)
add_car_image(cursor, 1,
              "https://cdn.proxyparts.com/vehicles/100012/6620067/large/3501ad31-7649-476b-a779-080936e33614.jpg")
add_car_image(cursor, 1, "https://m.wm.pl/2018/10/orig/img-20181026-170832-504235.jpg")
add_offer(cursor, 1, "BMW e36 funkiel new", "Very good condition, good car", 2, "e36", 23999.89)
add_car_details(cursor, 1, 32000, "diesel", 1598, 5, 1)
connection.commit()
connection.close()
