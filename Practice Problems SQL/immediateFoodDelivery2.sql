--Write your MySQL query statement below
WITH firstDelivery AS (
    SELECT
        customer_id, 
        customer_pref_delivery_date, 
        order_date
    FROM Delivery
    WHERE (customer_id, order_date) IN (
        SELECT customer_id, MIN(order_date)
        FROM Delivery
        GROUP BY customer_id
    )
)
SELECT ROUND(AVG(order_date = customer_pref_delivery_date) * 100, 2) AS immediate_percentage
FROM firstDelivery;