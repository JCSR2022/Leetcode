# Write your MySQL query statement below


select pr.product_id, round(coalesce(sum(us.units*pr.price)/sum(us.units),0),2) as average_price 
from Prices as pr
left join UnitsSold as us
on pr.product_id = us.product_id and us.purchase_date between pr.start_date and pr.end_date 
group by product_id;














-- us.product_id , pr.price
-- select *
-- from UnitsSold as us
-- left join Prices as pr
-- on us.product_id = pr.product_id;

-- select us.product_id, AVG( pr.price * us.units )
-- from Prices  as pr
-- left join UnitsSold as us
-- on us.product_id = pr.product_id
-- where us.purchase_date>=pr.start_date and us.purchase_date <= pr.end_date
-- group by us.product_id ;


-- select  us.product_id, round(sum(pr.price*us.units)/sum(us.units ),2) as average_price
-- from Prices  as pr
-- left join UnitsSold as us
-- on us.product_id = pr.product_id
-- where us.purchase_date>=pr.start_date and us.purchase_date <= pr.end_date
-- group by pr.product_id



-- SELECT
--     pr.product_id,
--     ROUND(
--         COALESCE(
--             SUM(pr.price * us.units) / SUM(us.units),
--             0
--         ),
--         2
--     ) AS average_price
-- FROM Prices AS pr
-- LEFT JOIN UnitsSold AS us
--     ON us.product_id = pr.product_id
--    AND us.purchase_date BETWEEN pr.start_date AND pr.end_date
-- GROUP BY pr.product_id;



-- -----------------------------------------------------------------------



-- select pr.product_id, round( COALESCE( sum(pr.price*us.units)/sum(us.units ) ,0 ) ,  2  ) as average_price
-- from prices as pr
-- left join UnitsSold  as us
-- on pr.product_id = us.product_id and us.purchase_date between pr.start_date and pr.end_date
-- group by pr.product_id;























