# Write your MySQL query statement below
#WITH managerTable AS ()
SELECT name
FROM Employee
WHERE id IN (SELECT DISTINCT managerId
FROM Employee
GROUP BY managerId
HAVING COUNT(id) >= 5
);