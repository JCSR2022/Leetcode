/* Write your T-SQL query statement below */
-- Asuming area [km2] and population [hab] . note:could be [mil2] or [Mhab]

select name, population, area
from World
where area >= 3000000 or population >= 25000000;
