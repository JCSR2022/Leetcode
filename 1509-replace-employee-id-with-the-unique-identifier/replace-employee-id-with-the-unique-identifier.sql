# Write your MySQL query statement below

select unique_id, e.name 
from  Employees as e
left join EmployeeUNI as eUNI on  e.id = eUNI.id;



