# Write your MySQL query statement below
SELECT
    t1.machine_id,
    ROUND(AVG(t1.end_time - t2.start_time), 3) AS processing_time
FROM
    (SELECT machine_id, process_id, timestamp AS end_time
     FROM Activity
     WHERE activity_type = 'end') t1
JOIN
    (SELECT machine_id, process_id, timestamp AS start_time
     FROM Activity
     WHERE activity_type = 'start') t2
ON
    t1.machine_id = t2.machine_id AND t1.process_id = t2.process_id
GROUP BY
    t1.machine_id
ORDER BY
    t1.machine_id;
