CREATE TABLE posts (
  id SERIAL PRIMARY KEY,
  title text,
  content text
);

CREATE TABLE comments (
  id SERIAL PRIMARY KEY,
  name text,
  content text,
  post_id int,
  constraint fk_post foreign key(post_id) references posts(id) on delete cascade
);

INSERT INTO posts (title, content) VALUES ("First Post", "Some content")

INSERT INTO comments (name, content, post_id) VALUES ("Tom", "This is a comment on the first post!", 1)
  
