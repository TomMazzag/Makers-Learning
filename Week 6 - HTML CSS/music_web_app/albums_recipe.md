# Single Table Design Recipe Template

# Request:
POST /albums

# With body parameters:
title=Voyage
release_year=2022
artist_id=2

# Expected response (200 OK)
(No content)

## 1. Extract nouns from the user stories or specification
```
Nouns:

album, title, release year, artist_id
```

## 2. Infer the Table Name and Columns

Put the different nouns in this table. Replace the example with your own nouns.

| Record                | Properties                     |
| --------------------- | ------------------------------ |
| album                 | title, release year, artist_id |

Name of the table (always plural): `albums`

Column names: `title`, `release_year`, `artist_id`

## 3. Decide the column types
```
# EXAMPLE:

id: SERIAL
title: text
release_year: int
artist_id: int
```

## 4. Write the SQL

```sql
-- EXAMPLE
-- file: albums_table.sql

-- Replace the table name, columm names and types.

CREATE TABLE albums (
  id SERIAL PRIMARY KEY,
  title text,
  release_year int,
  artist_id int
);
```

## 5. Create the table

```bash
psql -h 127.0.0.1 music_web_app < seeds/albums_table.sql
```