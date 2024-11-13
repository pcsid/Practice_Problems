--Write your MySQL query statement below
WITH valueTable AS (SELECT P.product_id, P.start_date, P.end_date, U.purchase_date, U.units, P.price
FROM Prices P
LEFT JOIN UnitsSold U ON P.product_id = U.product_id AND DATE(P.start_date) <= DATE(U.purchase_date) AND DATE(U.purchase_date) <= DATE(P.end_date))
SELECT V.product_id, ROUND(IFNULL(SUM(V.units * V.price)/SUM(V.units), 0), 2) AS average_price
FROM valueTable V
GROUP BY V.product_id
