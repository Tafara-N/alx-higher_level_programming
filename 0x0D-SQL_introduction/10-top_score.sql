-- A script that lists all records of the table second_table of the database
--  Results display both the score and the name (in that order)
--  Records are ordered by score (top first)
SELECT score, name
FROM second_table
ORDER BY score DESC;
