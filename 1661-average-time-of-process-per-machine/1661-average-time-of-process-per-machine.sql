# Write your MySQL query statement below

WITH machiens_process_times AS (
	SELECT 	a.machine_id, 
			a.process_id, 
			a.timestamp AS start_time,
			b.timestamp AS end_time,
			b.timestamp - a.timestamp AS process_time
	FROM Activity a 
	JOIN Activity b 
		ON a.machine_id = b.machine_id AND a.process_id = b.process_id
	WHERE a.activity_type = 'start' AND b.activity_type = 'end')
SELECT machine_id, ROUND(AVG(process_time),3) AS processing_time
FROM machiens_process_times
GROUP BY machine_id;