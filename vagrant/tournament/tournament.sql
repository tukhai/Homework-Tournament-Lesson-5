-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

--CREATE DATABASE tournament;
CREATE DATABASE tournament;
--\connect tournament
\c tournament

CREATE TABLE players(
    id serial PRIMARY KEY,
    name varchar(200),
    wins int DEFAULT 0,
    losses int DEFAULT 0,
    matches int DEFAULT 0
    );
CREATE TABLE match_1(
    id serial PRIMARY KEY,
    round int NOT NULL,
    a int, 
    b int, 
    winner int DEFAULT 0 
);
    