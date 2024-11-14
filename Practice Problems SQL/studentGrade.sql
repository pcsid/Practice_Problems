SELECT id, 
name, 
marks,
(CASE WHEN marks > 90 THEN "A+"
WHEN marks > 70 THEN "A"
WHEN marks > 50 THEN "B"
WHEN marks >= 40 THEN "C"
ELSE "Fail"
END AS grade)
FROM students;