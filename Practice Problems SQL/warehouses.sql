SELECT "owner of the smallest warehouse" AS metric,
C.name,
CONCAT(ROUND(W.width * W.length * 2.5, 2), " m^3") AS value
FROM customer 
INNER JOIN warehouse W ON C.id = W.customer_id
WHERE W.is_active = 1
ORDER BY value ASC
LIMIT 1

UNION ALL

SELECT "owner of the largest warehouse" AS metric,
C.name,
CONCAT(ROUND(W.width * W.length * 2.5, 2), " m^3") AS value
FROM customer C
INNER JOIN warehouse W ON C.id = W.customer_id
WHERE W.is_active = 1
ORDER BY value DESC
LIMIT 1

UNION ALL

SELECT "owner of the least number of warehouses" AS metric,
C.name,
COUNT(W.customer_id) AS value
FROM customer C
INNER JOIN warehouse W ON C.id = W.customer_id
WHERE W.is_active = 1
GROUP BY C.name
ORDER BY value ASC
LIMIT 1

UNION ALL

SELECT "owner of the most number of warehouses" AS metric,
C.name,
COUNT(W.customer_id) AS value
FROM customer C
INNER JOIN warehouse W ON C.id = W.customer_id
WHERE W.is_active = 1
GROUP BY C.name
ORDER BY value DESC
LIMIT 1