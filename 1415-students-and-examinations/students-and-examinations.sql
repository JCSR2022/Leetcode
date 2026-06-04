# Write your MySQL query statement below


-- SELECT st.student_id, st.student_name,  su.Subjects, sum(ex.subject_name) as attended_exams
-- FROM Students AS st
-- JOIN Subjects AS su , Examinations AS ex
-- ON  st.student_id = ex.student_id and su.subject_name = ex.subject_name
-- GROUP BY st.student_id, st.student_name,  su.Subjects;
-- NOOOOOOOOOOOOOOOOOOOOOO
--     --------------------------------------------------------------------------


-- SELECT
--     st.student_id,
--     st.student_name,
--     su.subject_name,
--     COUNT(ex.subject_name) AS attended_exams
-- FROM Students AS st
-- CROSS JOIN Subjects AS su
-- LEFT JOIN Examinations AS ex
--     ON st.student_id = ex.student_id
--    AND su.subject_name = ex.subject_name
-- GROUP BY
--     st.student_id,
--     st.student_name,
--     su.subject_name
-- ORDER BY
--     st.student_id,
--     su.subject_name;

-- SIIIIIIIIIIIIIIIIIIIIIII
-- --------------------------------------------------------------------



-- SELECT st.student_id, st.student_name, su.subject_name, ex.attended_exams
-- FROM(   SELECT student_id,subject_name,COUNT(*) as attended_exams
--         FROM Examinations
--         GROUP BY student_id, subject_name
-- )   AS ex
-- LEFT JOIN Students st ON  st.student_id = ex.student_id 
-- LEFT JOIN Subjects su ON su.subject_name = ex.subject_name
-- ORDER BY st.student_id, su.subject_name;

-- NOoooooooooooooooooooooo


SELECT
    st.student_id,
    st.student_name,
    su.subject_name,
    COALESCE(ex.attended_exams, 0) AS attended_exams
FROM Students st
CROSS JOIN Subjects su
LEFT JOIN (
    SELECT
        student_id,
        subject_name,
        COUNT(*) AS attended_exams
    FROM Examinations
    GROUP BY student_id, subject_name
) AS ex
    ON st.student_id = ex.student_id
   AND su.subject_name = ex.subject_name
ORDER BY
    st.student_id,
    su.subject_name;