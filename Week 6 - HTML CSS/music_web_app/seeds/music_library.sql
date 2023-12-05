DROP TABLE IF EXISTS albums;

CREATE TABLE albums (
  id SERIAL PRIMARY KEY,
  title text,
  release_year int,
  artist_id int
);

INSERT INTO albums (title, release_year, artist_id) VALUES ('Doolittle', 1989, 1);