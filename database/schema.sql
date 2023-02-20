DROP TABLE IF EXISTS cars;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS brands;
DROP TABLE IF EXISTS cars_images;
DROP TABLE IF EXISTS roles;
DROP TABLE IF EXISTS cars_details;

CREATE TABLE brands
(
    id    INTEGER PRIMARY KEY AUTOINCREMENT,
    brand TEXT NOT NULL
);

CREATE TABLE roles
(
    role TEXT PRIMARY KEY NOT NULL
);

CREATE TABLE users
(
    id       INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email    TEXT NOT NULL,
    password TEXT NOT NULL,
    role     TEXT,
    FOREIGN KEY (role) REFERENCES roles (role)
);

CREATE TABLE cars
(
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id     INTEGER NOT NULL,
    added       DATE    NOT NULL DEFAULT CURRENT_DATE,
    offer_name  TEXT    NOT NULL,
    description TEXT    NOT NULL,
    brand_id    INTEGER NOT NULL,
    car_model   TEXT,
    price       FLOAT   NOT NULL,
    FOREIGN KEY (brand_id) REFERENCES brands (id),
    FOREIGN KEY (user_id) REFERENCES users (id)
);
CREATE TABLE cars_images
(
    car_id    INTEGER NOT NULL,
    image_url TEXT    NOT NULL UNIQUE,
    FOREIGN KEY (car_id) REFERENCES cars (id)
);
CREATE TABLE cars_details
(
    car_id     INTEGER NOT NULL,
    mileage    TEXT    NOT NULL,
    fuel       TEXT    NOT NULL,
    engine_cap INTEGER NOT NULL,
    doors      INTEGER,
    gas        INTEGER NOT NULL DEFAULT 0,
    FOREIGN KEY (car_id) REFERENCES cars (id)
);