# Two Tables Design Recipe Template
```
As a blogger
So I can write interesting stuff
I want to write posts having a title.

As a blogger
So I can write interesting stuff
I want to write posts having a content.

As a blogger
So I can let people comment on interesting stuff
I want to allow comments on my posts.

As a blogger
So I can let people comment on interesting stuff
I want the comments to have a content.

As a blogger
So I can let people comment on interesting stuff
I want the author to include their name in comments.
```
## 1. Extract nouns from the user stories or specification

```
Nouns:

blogger, *posts*, title, content *coments*, conentent, bname
```

## 2. Infer the Table Name and Columns

| Record      | Properties        |
| ----------- | ----------------  |
| Post        | title, content    |
| Comments    | content, name     |

1. Name of the first table (always plural): `posts` 

    Column names: `title`, `content`

2. Name of the second table (always plural): `comments` 

    Column names: `content`, `name`

## 3. Decide the column types
```

Table: posts
id: SERIAL
title: text
content: text

Table: comments
id: SERIAL
name: text
content: text
```

## 4. Decide on The Tables Relationship
```

1. Can one post have many comments? YES
2. Can one comments have many posts? NO

-> Therefore,
-> A post HAS MANY comments
-> A comment BELONGS TO a post

-> Therefore, the foreign key is on the comments table.
```


## 5. Write the SQL

```sql
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
  constraint fk_post foreign key(post_id)
    references posts(id)
    on delete cascade
);

```



## 6. Create the tables

```bash
psql -h 127.0.0.1 blog < seeds/blogger_table.sql
```