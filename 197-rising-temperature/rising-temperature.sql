# Write your MySQL query statement below

#self-join .....


-- SELECT *,  DATE_ADD(w.recordDate, INTERVAL 1 DAY) as plusday
-- from weather as w;

SELECT   w1.id  -- w1.*, W2.*
FROM weather AS w1
JOIN weather AS w2
ON w1.recordDAte = DATE_ADD(w2.recordDate,INTERVAL 1 DAY)
WHERE w1.temperature > w2.temperature;
