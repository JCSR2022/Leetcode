# Write your MySQL query statement below

SELECT *
FROM Users
WHERE REGEXP_LIKE(mail,"^[A-Za-z][A-Za-z0-9_.-]*@leetcode[.]+com$")
ORDER BY user_id
