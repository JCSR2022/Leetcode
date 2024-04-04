# Write your MySQL query statement below

SELECT ROUND(SUM(tiv_2016),2) AS tiv_2016
FROM  (
    SELECT  tiv_2016,
            COUNT(*) OVER(PARTITION BY tiv_2015) AS count_same_tiv2015,
            COUNT(*) OVER(PARTITION BY  lat,lon) AS count_of_this_city
    FROM Insurance

      ) AS subquery
WHERE count_same_tiv2015 > 1 AND count_of_this_city = 1


