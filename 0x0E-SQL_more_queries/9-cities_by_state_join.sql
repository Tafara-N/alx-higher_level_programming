-- A script that lists all cities contained in the database hbtn_0d_usa
--  each record will display: cities.id - cities.name - states.name
--  results is sorted in ascending order by cities.id

SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states ON cities.state_id=states.id
ORDER BY cities.id ASC;