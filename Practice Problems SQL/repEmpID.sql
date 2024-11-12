# Write your MySQL query statement below
SELECT E.name, O.unique_id
FROM Employees E
LEFT JOIN EmployeeUNI O ON E.id = O.id;