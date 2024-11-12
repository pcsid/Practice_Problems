SELECT 
    machine_id,
    ROUND(AVG(end_time - start_time), 3) AS processing_time --get the average, round to 3 decimal
FROM (
    SELECT S.machine_id, S.timestamp AS start_time, E.timestamp as end_time --3 values to pull from
    FROM Activity S
    JOIN Activity E ON S.activity_type = "start" AND E.activity_type = "end" AND S.machine_id = E.machine_id AND S.process_id = E.process_id -- make start times and end times actual start times and end times, and match by machine and process id
) AS process_times --final table name
--Group by machine averages
GROUP BY machine_id;
