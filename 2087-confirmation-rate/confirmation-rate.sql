# Write your MySQL query statement below


-- COALESCE(ex.attended_exams, 0)



-- SELECT *
-- FROM (SELECT user_id , count(action) AS request
--     FROM Confirmations
--     GROUP BY user_id ) AS req
-- LEFT JOIN (SELECT user_id , count(action) AS confirm
--     FROM Confirmations 
--     WHERE action = 'confirmed'
--     GROUP BY user_id) AS conf
-- ON req.user_id = conf.user_id;

-- IF conf.confirm IS NULL THEN 0 ELSE conf.confirm  
-- ELECT user_id , CASE IS NULL THEN 0 ELSE COUNT(action)   AS confirm




-- SELECT req.user_id, req.request, CASE WHEN conf.confirm IS NULL THEN 0 ELSE conf.confirm END AS confirm
-- FROM (SELECT user_id , COUNT(action) AS request
--     FROM Confirmations
--     GROUP BY user_id ) AS req
-- LEFT JOIN (SELECT user_id , COUNT(action) AS confirm
--     FROM Confirmations 
--     WHERE action = 'confirmed'
--     GROUP BY user_id) AS conf
-- ON req.user_id = conf.user_id;


-- ------------------------------------------------------------------

-- SELECT sig.user_id, ROUND(conf_req.confirm/conf_req.request,2) as confirmation_rate
-- FROM (
--     SELECT req.user_id, req.request AS request , CASE WHEN conf.confirm IS NULL THEN 0 ELSE conf.confirm END AS confirm
--     FROM (SELECT user_id , COUNT(action) AS request
--         FROM Confirmations
--         GROUP BY user_id ) AS req
--     LEFT JOIN (SELECT user_id , COUNT(action) AS confirm
--         FROM Confirmations 
--         WHERE action = 'confirmed'
--         GROUP BY user_id) AS conf
--     ON req.user_id = conf.user_id) AS conf_req ;


--  --------------------------------------------------------------------------


-- SELECT sig.user_id, conf_req.confirm/conf_req.request as confirmation_rate
-- FROM Signups AS sig 
-- LEFT JOIN (
--     SELECT req.user_id, req.request AS request , CASE WHEN conf.confirm IS NULL THEN 0 ELSE conf.confirm END AS confirm
--     FROM (SELECT user_id , COUNT(action) AS request
--         FROM Confirmations
--         GROUP BY user_id ) AS req
--     LEFT JOIN (SELECT user_id , COUNT(action) AS confirm
--         FROM Confirmations 
--         WHERE action = 'confirmed'
--         GROUP BY user_id) AS conf
--     ON req.user_id = conf.user_id) AS conf_req 
-- ON sig.user_id  = conf_req.user_id ;


--  --------------------------------------------------------------------

-- SELECT ans.user_id , ROUND( CASE WHEN ans.confirmation_rate IS NULL THEN 0 ELSE ans.confirmation_rate END   , 2) AS confirmation_rate
-- FROM (
-- SELECT sig.user_id, conf_req.confirm/conf_req.request as confirmation_rate
-- FROM Signups AS sig 
-- LEFT JOIN (
--     SELECT req.user_id, req.request AS request , CASE WHEN conf.confirm IS NULL THEN 0 ELSE conf.confirm END AS confirm
--     FROM (SELECT user_id , COUNT(action) AS request
--         FROM Confirmations
--         GROUP BY user_id ) AS req
--     LEFT JOIN (SELECT user_id , COUNT(action) AS confirm
--         FROM Confirmations 
--         WHERE action = 'confirmed'
--         GROUP BY user_id) AS conf
--     ON req.user_id = conf.user_id) AS conf_req 
-- ON sig.user_id  = conf_req.user_id ) AS ans ;

-- MI SOLUCION DE MIERDA, FUNCIONA PERO ES UNA MIERDA!!!!
-- ----------------------------------------------------------------



SELECT s.user_id,
    ROUND( COALESCE( AVG(c.action = 'confirmed'),0 ), 2 ) AS confirmation_rate
FROM Signups s
LEFT JOIN Confirmations c
    ON s.user_id = c.user_id
GROUP BY s.user_id;


