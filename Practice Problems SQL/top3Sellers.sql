SELECT P.first_name, P.last_name, P.email, SUM(D.amount) AS total
FROM profiles P
JOIN deals D ON P.id = D.profile_id
WHERE D.dt BETWEEN "2022-06-01" AND "2022-06-30"
GROUP BY P.first_name, P.last_name, P.email
ORDER BY total DESC
LIMIT 3;