--Write your MySQL query statement below
WITH confirmationTable AS(
    SELECT S.user_id, 
    CASE
        WHEN C.action = "confirmed" THEN 1
        ELSE 0
    END AS Value
    FROM Signups S LEFT JOIN Confirmations C ON S.user_id = C.user_id)


SELECT ct.user_id, ROUND(SUM(ct.Value)/COUNT(ct.Value), 2) AS confirmation_rate
FROM confirmationTable ct
GROUP BY user_id