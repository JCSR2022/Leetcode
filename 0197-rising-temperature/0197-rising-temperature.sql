# Write your MySQL query statement below



with  compTemp as  (SELECT  *, 
                    LAG(temperature,1,1000) OVER (ORDER BY recordDate) AS prev_temp,  
                    LAG(recordDate,1,0) OVER (ORDER BY recordDate) AS prev_recordDate 
                    FROM Weather)
select id
from compTemp
where temperature - prev_temp > 0 and recordDate = DATE_ADD(prev_recordDate, INTERVAL 1 DAY);




/*

with  compTemp as  (SELECT  *, 
                    LAG(temperature,1,1000) OVER (ORDER BY recordDate) AS prev_temp  ,
                    LAG(recordDate,1,0) OVER (ORDER BY recordDate) AS prev_recordDate 
                    FROM Weather)
select *, prev_recordDate+1 as pre1 , recordDate = prev_recordDate+1 as BoolDates
from compTemp;
-- where temperature - prev_temp > 0 and recordDate = prev_recordDate+1;
*/
