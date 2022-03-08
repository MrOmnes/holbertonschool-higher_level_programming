-- Full Creation-- Create a table if not exists
CREATE TABLE IF NOT EXISTS second_table
(
    id int,
    name varchar(256),
	score int
);

INSERT into second_table (id, name, score) VALUES ('1', 'John', '10');
INSERT into second_table (id, name, score) VALUES ('2', 'Alex', '3');
INSERT into second_table (id, name, score) VALUES ('3', 'Bob', '14');
INSERT into second_table (id, name, score) VALUES ('4', 'George', '8');
