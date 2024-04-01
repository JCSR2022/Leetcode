# Write your MySQL query statement below

WITH scheduled_scheduled_table AS (
    SELECT *,
            RANK() OVER(PARTITION BY customer_id  ORDER BY order_date ) AS order_number,
            CASE WHEN order_date = customer_pref_delivery_date THEN 'immediate' ELSE 'scheduled' END AS orde_type
    FROM Delivery)
SELECT 
   ROUND(100*SUM(CASE WHEN orde_type = 'immediate' THEN 1 ELSE 0 END)/COUNT(order_number),2) AS immediate_percentage

FROM scheduled_scheduled_table
WHERE order_number = 1;
    


