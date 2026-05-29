# Write your MySQL query statement below


-- select v.customer_id, count( is null)
-- from visits as v
-- left join transactions as t
-- on v.visit_id = t.visit_id;



SELECT v.customer_id, COUNT(*) AS count_no_trans
FROM Visits AS v
LEFT JOIN Transactions AS t
ON v.visit_id = t.visit_id
WHERE t.transaction_id IS NULL
GROUP BY v.customer_id;




