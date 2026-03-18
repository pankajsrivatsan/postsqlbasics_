
DROP TABLE IF EXISTS staff;
CREATE TABLE staff1 (
    id      SERIAL PRIMARY KEY,
    name    VARCHAR(50)  NOT NULL,
    email   VARCHAR(100) UNIQUE NOT NULL,
    salary  INT          CHECK (salary >= 10000),
    city    VARCHAR(50)  DEFAULT 'mumbai'
);
