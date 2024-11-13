WITH student_subject AS ( -- Create first table
    SELECT s.student_id, s.student_name, sub.subject_name -- these vars from students
    FROM Students s
    CROSS JOIN Subjects sub -- cross join to get every student subject combo
)

SELECT ss.student_id, ss.student_name, ss.subject_name, 
       COUNT(e.student_id) AS attended_exams /*get count for student id, group by everything else to get unique for each student subject id combo*/
FROM student_subject ss
LEFT JOIN Examinations e /*the left join to incorporate examinations*/
ON ss.student_id = e.student_id AND ss.subject_name = e.subject_name
GROUP BY ss.student_id, ss.student_name, ss.subject_name
ORDER BY ss.student_id, ss.subject_name;
