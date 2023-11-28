# Single Table Design Recipe Template
```
As a person who loves movies,
So I can list all my favourite movies
I want to see a list of movies' titles.

As a person who loves movies,
So I can list all my favourite movies
I want to see a list of movies' genres.

As a person who loves movies,
So I can list all my favourite movies
I want to see a list of movies' release years.
```

## 1. Extract nouns from the user stories or specification

```
Nouns:

movies, title, genre, release year
```

## 2. Infer the Table Name and Columns

Put the different nouns in this table. Replace the example with your own nouns.

| Table      | Properties                  |
| ---------- | --------------------------- |
| Movies     | title, genre, release year  |

Name of the table (always plural): `movies`

Column names: `title`, `genre`, `release_year`

## 3. Decide the column types
```
id: SERIAL
title: text
genre: text
release_year: interval YEAR
```

## 4. Write the SQL

```sql

-- file: students_table.sql
CREATE TABLE movies (
  id SERIAL PRIMARY KEY,
  title text,
  genre text,
  release_year integer
);

```

## 5. Create the table

```bash
psql -h 127.0.0.1 movies_directory < Seeds/movies_table.sql
```

```sql
INSERT INTO movies (title, genre, release_year)
VALUES ('The Dark Knight', 'Action/crime', 2008);
```

