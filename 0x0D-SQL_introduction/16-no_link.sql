-- A script that lists all records of the table second_table
--  Don’t list rows without a name value
--  Results display the score and the name (in this order)
--  Records are listed by descending score

SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;