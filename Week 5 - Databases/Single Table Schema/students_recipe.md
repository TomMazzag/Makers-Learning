# Single Table Design Recipe Template
```
As a coach
So I can get to know all students
I want to see a list of students' names.

As a coach
So I can get to know all students
I want to see a list of students' cohorts.
```

## 1. Extract nouns from the user stories or specification

```
Nouns:

student, name, cohort
```

## 2. Infer the Table Name and Columns

Put the different nouns in this table. Replace the example with your own nouns.

| Table                 | Properties          |
| --------------------- | ------------------- |
| Student               | name, cohort        |

Name of the table (always plural): `students`

Column names: `name`, `cohort`

## 3. Decide the column types
```
id: SERIAL
name: text
cohort: text
```

## 4. Write the SQL

```sql

-- file: students_table.sql
CREATE TABLE students (
  id SERIAL PRIMARY KEY,
  name text,
  cohort text
);

```

## 5. Create the table

```bash
psql -h 127.0.0.1 student_directory_1 < students_table.sql
```
