-- List Cities
SELECT cities.id, states.name FROM cities, states WHERE states.name = 'California' AND states.id = cities.state_id
