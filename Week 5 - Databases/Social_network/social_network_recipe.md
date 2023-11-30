# Two Tables Design Recipe Template
```
As a social network user,
So I can have my information registered,
I'd like to have a user account with my email address.

As a social network user,
So I can have my information registered,
I'd like to have a user account with my username.

As a social network user,
So I can write on my timeline,
I'd like to create posts associated with my user account.

As a social network user,
So I can write on my timeline,
I'd like each of my posts to have a title and a content.

As a social network user,
So I can know who reads my posts,
I'd like each of my posts to have a number of views.
```
## 1. Extract nouns from the user stories or specification

```
Nouns:

user, account, email, username, posts, title and content, views
```

## 2. Infer the Table Name and Columns

| Record      | Properties               |
| ----------- | -----------------------  |
| user        | email address, username  |
| Post        | title, content, views    |


1. Name of the first table (always plural): `users` 

    Column names: `email_address`, `username`

2. Name of the second table (always plural): `posts` 

    Column names: `title`, `content`, `views`

## 3. Decide the column types
```

Table: users
id: SERIAL
email_address: text
username: text

Table: posts
id: SERIAL
title: text
content: text
views: integer
```

## 4. Decide on The Tables Relationship
```

1. Can one user have many posts? YES
2. Can one post have many users? NO

-> Therefore,
-> A user HAS MANY posts
-> A post BELONGS TO a user

-> Therefore, the foreign key is on the posts table.
```


## 5. Write the SQL

```sql
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

```



## 6. Create the tables

```bash
psql -h 127.0.0.1 social_network < seeds/social_network.sql
```