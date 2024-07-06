-- Rank countries by the number of fans for metal bands.
-- Import the table dump with columns: origin (country of origin) and nb_fans (number of fans).

SELECT origin, SUM(fans) as nb_fans FROM metal_bands
GROUP BY origin ORDER BY nb_fans DESC;
