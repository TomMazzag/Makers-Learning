DROP TABLE IF EXISTS users;

CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  name text,
  username text,
  email text,
  password text
);

INSERT INTO users (name, username, email, password) VALUES ('Anonymous', 'AnonymousUser', 'anon@user.com', Null);