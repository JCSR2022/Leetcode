# Write your MySQL query statement below


SELECT  
        IF( se.id < (SELECT MAX(id) FROM Seat),
                    IF(se.id%2 = 0, se.id-1,se.id+1),
                    IF(se.id%2 = 0, se.id-1,se.id)) AS id,
        se.student
FROM Seat se
ORDER BY id


