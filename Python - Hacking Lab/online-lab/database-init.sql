
CREATE DATABASE test;
GRANT ALL PRIVILEGES ON DATABASE test TO postgres;

CREATE DATABASE main;
GRANT ALL PRIVILEGES ON DATABASE main TO postgres;

\c main;

CREATE TABLE "user" (
    id      SERIAL PRIMARY KEY,
    name    varchar(50),
    surname varchar(50),
    password varchar(50)
);

INSERT INTO "user" (name, surname, password)
VALUES ('serhat', 'sonmez', '12345'), ('admin', 'admin', '12345'), ('foo', 'bar', '12345');