-- The job of this file is to reset all of our important database tables.
-- And add any data that is needed for the tests to run.
-- This is so that our tests, and application, are always operating from a fresh
-- database state, and that tests don't interfere with each other.

-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS recipies;
DROP SEQUENCE IF EXISTS recipeis_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS recipeis_id_seq;
CREATE TABLE recipies (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    average_cooking_time INTEGER,
    rating INTEGER
);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO recipies (name, average_cooking_time, rating) VALUES ('Pizza', 10 , 5);
INSERT INTO recipies (name, average_cooking_time, rating) VALUES ('Spaghetti', 15 , 3);
INSERT INTO recipies (name, average_cooking_time, rating) VALUES ('Chilli', 20 , 4);
INSERT INTO recipies (name, average_cooking_time, rating) VALUES ('Wrap', 5 , 2);
INSERT INTO recipies (name, average_cooking_time, rating) VALUES ('Sandwich', 1 , 4);
