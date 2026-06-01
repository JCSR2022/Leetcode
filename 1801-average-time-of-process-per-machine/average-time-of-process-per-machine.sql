# Write your MySQL query statement below


-- SELECT  act1.machine_id,  act2.process_id ,  act2.timestamp as starTime ,act1.timestamp as endTime 
-- from activity as act1
-- JOIN activity as act2
-- ON act1.machine_id = act2.machine_id and act1.process_id = act2.process_id
-- WHERE act1.activity_type = 'end' and act2.activity_type = 'start';


SELECT  act1.machine_id, ROUND( AVG(act1.timestamp  - act2.timestamp),3) as processing_time
from activity as act1
JOIN activity as act2
ON act1.machine_id = act2.machine_id and act1.process_id = act2.process_id
WHERE act1.activity_type = 'end' and act2.activity_type = 'start'
GROUP BY act1.machine_id;

