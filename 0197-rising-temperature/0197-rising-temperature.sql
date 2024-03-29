# Write your MySQL query statement below

-- Sol at: 
SELECT w1.id -- , w1.recordDate , w1.temperature , w2.recordDate as prevRecordDate , w2.temperature as prevTemperature 
FROM Weather w1
JOIN Weather w2 ON DATEDIFF(w2.recordDate, w1.recordDate ) = -1 
where w1.temperature > w2.temperature;

-- My sol: 
/*
with  compTemp as  (SELECT  *, 
                    LAG(temperature,1,1000) OVER (ORDER BY recordDate) AS prev_temp,  
                    LAG(recordDate,1,0) OVER (ORDER BY recordDate) AS prev_recordDate 
                    FROM Weather)
select id
from compTemp
where temperature - prev_temp > 0 and recordDate = DATE_ADD(prev_recordDate, INTERVAL 1 DAY);

*/


