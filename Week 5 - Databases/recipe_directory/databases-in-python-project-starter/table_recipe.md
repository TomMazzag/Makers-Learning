# Single Table Design Recipe Template
```
As a food lover,
So I can stay organised and decide what to cook,
I'd like to keep a list of all my recipes with their names.

As a food lover,
So I can stay organised and decide what to cook,
I'd like to keep the average cooking time (in minutes) for each recipe.

As a food lover,
So I can stay organised and decide what to cook,
I'd like to give a rating to each of the recipes (from 1 to 5).
```

## 1. Extract nouns from the user stories or specification

```
Nouns:

recipe, name, average cooking time, rating
```

## 2. Infer the Table Name and Columns

Put the different nouns in this table. Replace the example with your own nouns.

| Table   | Properties                         |
| ------- | ---------------------------------- |
| recipe  | name, average cooking time, rating |

Name of the table (always plural): `recipies`

Column names: `name`, `average_cooking_time`, `rating`

## 3. Decide the column types
```
id: SERIAL
name: text
average_cooking_time: integer
rating: text
```

## 4. Write the SQL

```sql

-- file: recipies.sql
CREATE TABLE recipies (
  id SERIAL PRIMARY KEY,
  name text,
  average_cooking_time integer,
  rating integer
);

```

## 5. Create the table

```bash
psql -h 127.0.0.1 recipe_directory < seeds/recipes.sql
```
