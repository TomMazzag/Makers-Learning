# Two Tables Design Recipe Template
```
As a coach
So I can get to know all students
I want to see a list of students' names.

As a coach
So I can get to know all students
I want to see a list of cohorts' names.

As a coach
So I can get to know all students
I want to see a list of cohorts' starting dates.

As a coach
So I can get to know all students
I want to see a list of students' cohorts.
```
## 1. Extract nouns from the user stories or specification

```
Nouns:

student, name, cohort, cohort name, start date
```

## 2. Infer the Table Name and Columns

| Record      | Properties          |
| ----------- | ------------------  |
| Students    | name, cohort        |
| Cohort      | name, start date    |

1. Name of the first table (always plural): `students` 

    Column names: `name`, `cohort`

2. Name of the second table (always plural): `cohorts` 

    Column names: `name`, `start_date`

## 3. Decide the column types
```

Table: students
id: SERIAL
name: text
cohort: int

Table: cohorts
name: SERIAL
start_date: text
```

## 4. Decide on The Tables Relationship
```

1. Can one student have many cohorts? NO
2. Can one cohort have many students? YES

-> Therefore,
-> A cohort HAS MANY students
-> A student BELONGS TO a cohort

-> Therefore, the foreign key is on the students table.
```


## 5. Write the SQL

```sql
CREATE TABLE cohorts (
  id SERIAL PRIMARY KEY,
  name text,
  start_date text
);

CREATE TABLE students (
  id SERIAL PRIMARY KEY,
  name text,
  cohort_id int,
  constraint fk_cohort foreign key(cohort_id)
    references cohorts(id)
    on delete cascade
);

```



## 6. Create the tables

```bash
psql -h 127.0.0.1 student_directory_2 < seeds/students_table.sql
```