-- List Cities
SELECT * FROM cities JOIN states ON states.id = cities.state_id ORDER BY cities.id ASC