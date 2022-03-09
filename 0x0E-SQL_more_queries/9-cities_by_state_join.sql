-- List Cities
SELECT cities.name, cities.id, states.id FROM cities JOIN states ON states.id = cities.state_id ORDER BY cities.id ASC
