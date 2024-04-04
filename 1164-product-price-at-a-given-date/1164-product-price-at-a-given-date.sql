# Write your MySQL query statement below

WITH cte AS (
SELECT *,
  RANK() OVER (PARTITION BY product_id ORDER BY change_date DESC) AS rank_dates
FROM Products
WHERE change_date <= '2019-08-16'
ORDER BY change_date)

SELECT  product_id,new_price AS Price
FROM cte 
WHERE rank_dates = 1

UNION
SELECT product_id, 10 AS Price
FROM Products
WHERE product_id NOT IN (SELECT product_id FROM cte )