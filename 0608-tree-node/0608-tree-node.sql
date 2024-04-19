# Write your MySQL query statement below


SELECT id,
       CASE
           WHEN p_id IS NULL THEN 'Root'
           WHEN id NOT IN (SELECT DISTINCT p_id FROM Tree where p_id is not null) THEN 'Leaf'
           ELSE 'Inner'
       END AS type
FROM Tree;
