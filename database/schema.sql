DROP TABLE IF EXISTS cars;
DROP TABLE IF EXISTS brands;
DROP TABLE IF EXISTS cars_images;

CREATE TABLE brands
(
    id    INTEGER PRIMARY KEY AUTOINCREMENT,
    brand TEXT NOT NULL
);

CREATE TABLE cars
(
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    added       DATE    NOT NULL DEFAULT CURRENT_DATE,
    offer_name  TEXT    NOT NULL,
    description TEXT    NOT NULL,
    brand_id    INTEGER NOT NULL,
    car_model   TEXT,
    price       FLOAT   NOT NULL,
    FOREIGN KEY (brand_id) REFERENCES brands (id)
);
CREATE TABLE cars_images
(
    car_id    INTEGER NOT NULL,
    image_url TEXT    NOT NULL UNIQUE,
    FOREIGN KEY (car_id) REFERENCES cars (id)
)
