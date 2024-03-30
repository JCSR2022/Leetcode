# Write your MySQL query statement below

SELECT a.student_id, a.student_name, b.subject_name, count(c.subject_name) as attended_exams
FROM students as a
JOIN Subjects as b   
LEFT JOIN Examinations as c ON a.student_id = c.student_id AND b.subject_name = c.subject_name
GROUP BY a.student_id, b.subject_name
ORDER BY a.student_id, b.subject_name;