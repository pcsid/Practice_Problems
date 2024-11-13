--Write your MySQL query statement below
SELECT A.employee_id, A.name, COUNT(B.reports_to) AS reports_count, ROUND(AVG(B.age), 0) AS average_age
FROM Employees A
JOIN Employees B
ON A.employee_id = B.reports_to
GROUP BY A.employee_id
ORDER BY A.employee_id