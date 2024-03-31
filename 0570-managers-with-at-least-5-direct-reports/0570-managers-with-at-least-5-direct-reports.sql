# Write your MySQL query statement below


WITH ManagersDirectreports AS ( SELECT managerId, COUNT(managerId) AS directReported
FROM Employee
WHERE managerId IS NOT NULL
GROUP BY managerId)
SELECT em.name 
FROM Employee em
JOIN ManagersDirectreports md ON md.managerId = em.id
WHERE md.directReported >= 5;




