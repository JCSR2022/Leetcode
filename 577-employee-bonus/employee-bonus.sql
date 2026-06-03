# Write your MySQL query statement below


SELECT e.name , b.bonus
FROM Employee as e
LEFT JOIN Bonus as b 
ON e.empID = b.empID
WHERE b.bonus IS null or b.bonus < 1000;  