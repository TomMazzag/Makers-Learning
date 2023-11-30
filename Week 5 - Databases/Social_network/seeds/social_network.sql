DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS posts;

CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  email_address text,
  username text
);

CREATE TABLE posts (
  id SERIAL PRIMARY KEY,
  title text,
  content text,
  views int,
  user_id int,
  constraint fk_user foreign key(user_id)
    references users(id)
    on delete cascade
);

INSERT INTO users (email_address, username) VALUES ('example@test.com', 'Person1');
INSERT INTO users (email_address, username) VALUES ('example@makers.com', 'Person2');
INSERT INTO users (email_address, username) VALUES ('example@databases.com', 'Person3');

INSERT INTO posts (title, content, views, user_id) VALUES ('First post', 'This is a first post', 19, 1);
INSERT INTO posts (title, content, views, user_id) VALUES ('Second post', 'This is a second post', 9, 1);
INSERT INTO posts (title, content, views, user_id) VALUES ('Third post', 'This is a third post', 15, 1);
INSERT INTO posts (title, content, views, user_id) VALUES ('Fourth post', 'This is a fourth post', 3, 2);