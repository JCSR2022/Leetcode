/* Write your T-SQL query statement below */
/*
SELECT *
FROM Users
WHERE mail LIKE '[A-Za-z]%'
  AND mail LIKE '%@leetcode%.com'
  AND mail NOT LIKE '%[#]%'
ORDER BY user_id;
'^[A-Za-z][A-Za-z0-9_.-]*@leetcode[.]+com$'
*/



/*
SELECT *
FROM Users
WHERE mail LIKE '[A-Za-z]%[A-Za-z0-9.-!_]@leetcode.com' ESCAPE '!' AND
       NOT LIKE '%#%' 
ORDER BY user_id;

*/
/*
SELECT mail
FROM Users
WHERE mail LIKE '[A-Za-z][A-Za-z0-9.-_]%@leetcode.com'
ORDER BY user_id;
*/

/*
SELECT mail
FROM Users
WHERE mail  LIKE '[A-Za-z]%[A-Za-z0-9.-_][A-Za-z0-9.-_][A-Za-z0-9.-_][A-Za-z0-9.-_]@leetcode.com';



-- select PATINDEX('%[^A-Za-z0-9@._-]%',mail);

SELECT LEN(mail) - LEN(REPLACE(mail, '@', '')) AS cantidad_apariciones_a
FROM Users;
*/


SELECT *
FROM Users
WHERE mail LIKE '[A-Za-z]%@leetcode.com'
AND PATINDEX('%[^A-Za-z0-9@._-]%',mail) = 0
AND LEN(mail) - LEN(REPLACE(mail, '@', '')) = 1
ORDER BY user_id ;





/*
SELECT user_id, name, mail
FROM Users
WHERE 
    CASE WHEN CHARINDEX('@', mail) = 0 THEN 0 ELSE 1 END = 1
    AND CASE WHEN LEN(mail) - LEN(REPLACE(mail, '@', '')) = 1 THEN 1 ELSE 0 END = 1
    AND CASE WHEN LEFT(mail, 1) LIKE '[A-Za-z]' THEN 1 ELSE 0 END = 1
    AND RIGHT(mail, LEN(mail) - CHARINDEX('@', mail)) = '@leetcode.com'
   -- AND mail NOT LIKE '%[^A-Za-z0-9_.-]%'
ORDER BY user_id;


*/

/*
WHERE RIGHT(mail, LEN(mail) - CHARINDEX('@', mail)) = '@leetcode.com' AND
      SUBSTRING(mail, 1, CHARINDEX('@', mail) - 1) LIKE '[A-Za-z][A-Za-z0-9_.-]%'
ORDER BY user_id;
*/





