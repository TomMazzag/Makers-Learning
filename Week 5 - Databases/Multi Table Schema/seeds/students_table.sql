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
